# Strobes Automation Pipelines

## Overview

Strobes Automation Pipelines is a powerful feature that allows users to write custom logic for processing and enriching vulnerability data within the Strobes platform. These pipelines can be integrated into automation workflows to enhance the triage process, improve data quality, and streamline security operations.

## Features

- Custom Python scripts for data processing
- Integration with Strobes Automation workflows
- Access to comprehensive asset and finding data fields
- Flexible output for updating Strobes entities

## Getting Started

### Prerequisites

- Access to Strobes platform
- Basic knowledge of Python programming

### Writing Your First Pipeline

1. Navigate to the Automation section in Strobes
2. Create a new automation or edit an existing one
3. In the "Pipelines" step, you'll find a code editor
4. Write your pipeline logic using the `run_pipeline(input)` function

Example:

```python
def run_pipeline(input):
    if "critical" in input.title.lower():
        output = {
            "severity": "Critical",
            "tags": ["high-priority", "needs-immediate-attention"]
        }
    else:
        output = {
            "severity": input.severity,
            "tags": ["standard-process"]
        }
    return output
```

## Pipeline Input

The `input` object provides access to all fields of the current asset or finding. Refer to the Strobes API documentation for a complete list of available fields.

## Pipeline Output

The `output` dictionary returned by your pipeline can include any fields you wish to update on the asset or finding. Common uses include:

- Updating severity or priority
- Adding or modifying tags
- Setting custom fields
- Triggering additional actions

## Best Practices

1. Keep pipelines modular and focused on specific tasks
2. Use descriptive variable names and add comments for complex logic
3. Handle exceptions gracefully to prevent workflow disruptions
4. Test pipelines thoroughly before deploying to production

## Example Use Cases

1. CVSS Score-Based Severity Adjustment
2. Exploit Availability Impact Assessment
3. Zero-Day Vulnerability Prioritization
4. SLA Violation Risk Calculation
5. CWE-Based Vulnerability Categorization

## Contributing

We welcome contributions to improve and expand our pipeline examples. Please submit a pull request with your proposed changes.

## Support

For questions or issues related to Strobes Automation Pipelines, please contact our support team at support@strobes.co.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
