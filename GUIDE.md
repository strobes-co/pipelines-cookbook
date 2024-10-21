# Strobes Pipeline Attribute Guide

## Introduction

In Strobes pipelines, you have access to a wide range of attributes for both assets and findings (bugs). These attributes allow you to create powerful, customized workflows for processing your security data. This guide will help you understand how to use these attributes effectively in your pipeline scripts.

## How to Access Attributes

In your pipeline script, you can access attributes of the current asset or finding using dot notation on the `input` object. For example:

- To access the title of a finding: `input.title`
- To access the name of an asset: `input.name`

For related objects or prefetched fields, you can chain the dot notation:
- To access the name of the asset associated with a finding: `input.asset.name`
- To access CVE information for a finding: `input.prefetched_cve[0].cve_id`

## Examples

### Example 1: Adjusting Finding Severity Based on CVE Score

```python
def run_pipeline(input):
    if input.prefetched_cve:
        cve = input.prefetched_cve[0]
        if cve.cvss >= 9.0:
            return {"severity": 5}  # Set to Critical
        elif cve.cvss >= 7.0:
            return {"severity": 4}  # Set to High
    return {}  # No change if no CVE or lower score
```

### Example 2: Tagging Assets Based on Cloud Type

```python
def run_pipeline(input):
    cloud_tags = {
        2: "aws",
        3: "azure",
        4: "gcp"
    }
    if input.cloud_type in cloud_tags:
        return {"tags": input.prefetched_asset_tags + [cloud_tags[input.cloud_type]]}
    return {}
```

## Asset Attributes

### Direct Attributes
- id
- name
- target
- exposed (1: Public, 2: Private)
- type (Various asset types)
- cloud_type (1: Others, 2: AWS, 3: Azure, 4: GCP)
- disabled
- sensitivity (0: None, 1: Low, 2: Medium, 3: High, 4: Critical)
- is_active
- created
- updated
- location
- region
- resource_id
- account_id
- fields (custom fields)
- dns_info
- whois_info
- asn
- waf
- cdn
- asm_last_alive

### Related Attributes
- connector.name
- created_by.username
- organization.name

### Prefetched Fields
- prefetched_asset_tags (list of tag objects)

## Finding (Bug) Attributes

### Direct Attributes
- id
- title
- description
- mitigation
- steps_to_reproduce
- state (0: New, 1: Active, 2: Resolved, 3: Duplicate, 4: Not Applicable, 5: Committed, 6: Accepted Risk, 7: Won't Fix)
- severity (1: Info, 2: Low, 3: Medium, 4: High, 5: Critical)
- bug_level (1: Code, 2: Web, 3: Mobile, 4: Network, 5: Cloud, 6: Package)
- alert_category (Various categories)
- cvss
- attack_vector
- due_date
- sla_violated
- has_user_defined_due_date
- exploit_available
- exploit_info
- patch_available
- patch_info
- prioritization_score
- drill_down_score
- vulnerable_since
- zero_day_available
- is_wormable
- trend (1: Low, 2: Medium, 3: High, 4: Ultra, 5: Extreme)
- advisories_seen
- epss_score
- cisa_due_date
- records_at_risk
- records_type (1: PII, 2: PHI, 3: PCI, 4: GDPR, 5: Other)
- fields (custom fields)
- links
- is_misconfiguration
- sla_rule_search_query
- created
- updated
- is_active
- is_alert

### Related Attributes
- asset.name
- connector.name
- connector_config.name
- team.name
- reported_by.username
- organization.name

### Prefetched Fields
- prefetched_cve (list of CVE objects)
- prefetched_cwe (list of CWE objects)
- prefetched_finding_tags (list of tag objects)
- prefetched_assigned_to (list of user objects)
- prefetched_finding_attachments (list of attachment objects)
- prefetched_engagements (list of engagement objects)
- prefetched_nist (list of NIST control objects)
- prefetched_owasp (list of OWASP category objects)

## Accessing Custom Fields

Custom fields can be accessed using the `fields` attribute:

```python
def run_pipeline(input):
    custom_value = input.fields.get("custom_field_slug")
    return {"description": f"Custom field value: {custom_value}"}
```

Remember, the availability of some fields may depend on the context and configuration of your Strobes instance. Always test your pipelines thoroughly to ensure they work as expected with your data.
