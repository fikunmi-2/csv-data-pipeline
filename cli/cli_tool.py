# This is the cli_tool file that we will use to call our already created pipeline.

import argparse
import json
import sys

from pipeline.data_analyzer import analyze_data
from pipeline.dataset_formatter import format_output

def main():

   parser = argparse.ArgumentParser(
       description="CSV Data Processing Pipeline: clean, analyze and format data.",
   )

   parser.add_argument("filename", type=str, help="Path to the input CSV file")
   parser.add_argument("-m", "--mode", default="human", choices=["human", "machine"],
                       help="Output Format: human-readable or machine-readable")
   parser.add_argument("-o", "--output", type=str, default="output.json")

   args = parser.parse_args()

   analyzed_data = analyze_data(args.filename)

   if analyzed_data["Status"] == "Failure":
       print(f"Error: {analyzed_data['Error']}")
       sys.exit(1)

   output = format_output(analyzed_data, mode=args.mode)

   if args.mode == "machine":
       print(json.dumps(output, indent=2))
   else:
       print(output["result"])

if __name__ == "__main__":
    main()