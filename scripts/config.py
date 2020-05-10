#!/usr/bin/env python

#This config is to customise the overall project options; config.yml is for the icon config


# This prefixes file names e.g. the AWS part of AWSCommon.puml, AWSSimplified.puml and puml macros e.g. AWSEntity, AWSEntityColoring
PREFIX = "AWS"


TEMPLATE_DEFAULT = """
Defaults:
  Colors:
    SquidInk: "#232F3E"
  # Defaults for all categories
  Category:
    Color: SquidInk
  # Maximum in either height or width in pixels
  TargetMaxSize: 64
"""

MARKDOWN_PREFIX_TEMPLATE = """
# AWS Symbols

The table below lists all AWS symbols in the `dist/` directory, sorted by category.

If you want to reference and use these files without Internet connectivity, you can also download the whole [*PlantUML Icons for AWS* dist](dist/) directory and reference it locally with PlantUML.

## PNG images

For each symbol, there is a resized icon in PNG format generated from the source file. Where the original icons had transparency set, this has been kept in the generated icons. You can also use the images outside of PlantUML, e.g. for documents or presentations, but the official [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/) are available in all popular formats.

## All PNG generated AWS symbols

Category | PUML Macro (Name) | Image (PNG) | PUML Url
  ---    |  ---  | :---:  | ---
"""

PUML_COPYRIGHT = ""

PUML_LICENSE_HEADER = ""