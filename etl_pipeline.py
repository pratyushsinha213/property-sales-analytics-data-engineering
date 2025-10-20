from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import time

class ETLPipeline:
    def __init__(self, input_path="./raw-data", output_path="./processed-data"):
        self.input_path = input_path
        self.output_path = output_path
        self.spark = SparkSession.builder.master("local[*]").appName("PropertyETLTransformations").getOrCreate()

    def read_data(self, file_name):
        """Read CSV file"""
        df = (
            self.spark.read.format("csv")
            .option("header", True)
            .option("inferSchema", True)
            .load(f"{self.input_path}/{file_name}")
        )
        return df

    def clean_columns(self, df):
        """Clean column names and rename for consistency"""
        df = df.drop(f.col("previous_owners"))
        return df

    def create_dimensions(self, df):
        """Create all dimension tables"""
        dim_property = (
            df.select(
                "property_type",
                "furnishing_status",
                "rooms",
                "bathrooms",
                "garage",
                "garden",
                "property_size_sqft"
            )
            .dropDuplicates()
            .withColumn("property_type_key", f.monotonically_increasing_id())
        )

        dim_location = (
            df.select(
                "country",
                "city",
                "crime_cases_reported",
                "legal_cases_on_property",
                "neighbourhood_rating",
                "connectivity_score"
            )
            .dropDuplicates()
            .withColumn("location_key", f.monotonically_increasing_id())
        )

        dim_customer_financials = (
            df.select(
                "customer_salary",
                "loan_amount",
                "loan_tenure_years",
                "monthly_expenses",
                "emi_to_income_ratio"
            )
            .dropDuplicates()
            .withColumn("customer_financial_key", f.monotonically_increasing_id())
        )

        return dim_property, dim_location, dim_customer_financials

    def create_fact_table(self, df, dims):
        """Join dimensions and create fact table"""
        dim_property, dim_location, dim_customer_financials = dims

        fact_property_purchase = (
            df
            .join(dim_property,
                  on=[
                      "property_type",
                      "furnishing_status",
                      "rooms",
                      "bathrooms",
                      "garage",
                      "garden",
                      "property_size_sqft"
                  ],
                  how="left"
                  )
            .join(dim_location,
                  on=[
                      "country",
                      "city",
                      "crime_cases_reported",
                      "legal_cases_on_property",
                      "neighbourhood_rating",
                      "connectivity_score"
                  ],
                  how="left"
                  )
            .join(dim_customer_financials,
                  on=[
                      "customer_salary",
                      "loan_amount",
                      "loan_tenure_years",
                      "monthly_expenses",
                      "emi_to_income_ratio"
                  ],
                  how="left"
                  )
            .select(
                "property_id",
                "price",
                "down_payment",
                "decision",
                "property_type_key",
                "location_key",
                "customer_financial_key"
            )
        )

        return fact_property_purchase

    def write_parquet(self, df, name, mode="append"):
        """Write data in Parquet format"""
        df.write.format("parquet").mode(mode).save(f"{self.output_path}/{name}")

    def run(self, file_name):
        """Run full ETL for a single file"""
        print(f"Processing {file_name}...")

        start_time = time.time()

        df = self.read_data(file_name)
        df = self.clean_columns(df)
        dims = self.create_dimensions(df)
        fact_property_purchase = self.create_fact_table(df, dims)

        # Write to output
        # Append mode is done for the fact table where as Overwrite is done for the dimension tables
        self.write_parquet(fact_property_purchase, "fact_property_purchase", mode="append")
        self.write_parquet(dims[0], "dim_property", mode="overwrite")
        self.write_parquet(dims[1], "dim_location", mode="overwrite")
        self.write_parquet(dims[2], "dim_customer_financials", mode="overwrite")

        end_time = time.time()
        process_time = end_time - start_time

        print(f"✅ Finished processing {file_name} in {round(process_time, 2)} seconds.")


if __name__ == "__main__":
    etl = ETLPipeline()
    files = [
        "data_01.csv", "data_02.csv", "data_03.csv", "data_04.csv", "data_05.csv",
        "data_06.csv", "data_07.csv", "data_08.csv", "data_09.csv", "data_10.csv",
    ]
    for file in files:
        etl.run(file)

    # etl.run("FILE_NAME")