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
- type [various asset types](#asset-types)
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
#### prefetched_asset_tags (list of tag objects)
- `id` (AutoField) - Primary key
- `slug` (SlugField) - URL-friendly version of name
- `name` (CharField) - Tag name
- `created` (DateTimeField) - Creation timestamp
- `updated` (DateTimeField) - Update timestamp

### Asset Types
- `web`= 1
- `mobile`= 2
- `network`= 3
- `cloud`= 4
- `website`= 5
- `api_service`= 6
- `code_repo`= 7
- `web_server`= 8
- `db_server`= 9
- `container`= 10
- `container_image`= 11
- `firewall`= 12
- `router`= 13
- `switch`= 14
- `network_hub`= 15
- `printer`= 16
- `generic_server`= 17
- `wap`= 18
- `mail_server`= 19
- `dns_server`= 20
- `dhcp_server`= 21
- `endpoint`= 22
- `network_storage`= 23
- `vm`= 24
- `aws_api_gateway`= 25
- `aws_cloudfront`= 26
- `aws_cloudwatch`= 27
- `aws_dynamodb`= 28
- `aws_ebs`= 29
- `aws_ec2`= 30
- `aws_ecr`= 31
- `aws_ecs`= 32
- `aws_efs`= 33
- `aws_eks`= 34
- `aws_opensearch`= 35
- `aws_qldb`= 36
- `aws_route_53`= 37
- `aws_sagemaker`= 38
- `aws_simple_notification_service`= 39
- `aws_simple_queue_service`= 40
- `aws_s3`= 41
- `aws_vpc`= 42
- `aws_cloudformation`= 43
- `aws_cloudtrail`= 44
- `aws_cloudbuild`= 45
- `aws_config`= 46
- `aws_elastic_bean_stalk`= 47
- `aws_key_management_service`= 48
- `aws_secrets_manager`= 49
- `aws_shield`= 50
- `aws_auto_scaling`= 51
- `aws_waf`= 52
- `aws_data_migration_service`= 53
- `aws_elb`= 54
- `aws_emr`= 55
- `aws_guard_duty`= 56
- `aws_iam`= 57
- `aws_codebuild`= 58
- `aws_lambda`= 59
- `aws_rds`= 60
- `aws_redshift_v2`= 61
- `aws_ssm`= 62
- `gcp_big_query`= 63
- `gcp_compute_engine`= 64
- `gcp_dns`= 65
- `gcp_iam`= 66
- `gcp_ckm`= 67
- `gcp_cloud_logging`= 68
- `gcp_cloud_sql`= 69
- `gcp_cloud_storage`= 70
- `azure_compute`= 71
- `azure_container_instances`= 72
- `azure_iam`= 73
- `azure_key_vault`= 74
- `azure_firewall`= 75
- `azure_lb`= 76
- `azure_waf`= 77
- `azure_dns`= 78
- `azure_active_directory`= 79
- `azure_sql_db`= 80
- `azure_blob_storage`= 81
- `azure_cosmos_db`= 82
- `azure_kubernetes_service`= 83
- `azure_container_registry`= 84
- `azure_files`= 85
- `azure_managed_disks`= 86
- `azure_private_link`= 87
- `package`= 88
- `aws_app_runner`= 89
- `aws_batch`= 90
- `aws_ec2_image_builder`= 91
- `aws_lightsail`= 92
- `aws_sar`= 93
- `aws_documentdb`= 94
- `aws_elasticache`= 95
- `aws_keyspaces`= 96
- `aws_memorydb`= 97
- `aws_neptune`= 98
- `aws_security_groups`= 99
- `aws_certificate_manager`= 100
- `aws_cloudhsm`= 101
- `aws_cognito`= 102
- `aws_detective`= 103
- `aws_directory_service`= 104
- `aws_inspector`= 105
- `aws_macie`= 106
- `aws_ram`= 107
- `aws_security_hub`= 108
- `aws_backup`= 109
- `aws_edr`= 110
- `aws_fsx`= 111
- `aws_s3_glacier`= 112
- `aws_mq`= 113
- `aws_redshift`= 114
- `aws_auto_scaling_group`= 115
- `aws_auto_scaling_launch_configuration`= 116
- `aws_auto_scaling_scaling_policy`= 117
- `aws_backup_vault`= 118
- `aws_backup_plan`= 119
- `aws_cloudformation_type`= 120
- `aws_cloudformation_stack`= 121
- `aws_cloudfront_distribution`= 122
- `aws_cloudfront_streaming_distribution`= 123
- `aws_cloudfront_functions`= 124
- `aws_cloudhsm_hsm`= 125
- `aws_cloudhsm_hapg`= 126
- `aws_codebuild_build`= 127
- `aws_codebuild_project`= 128
- `aws_codebuild_report`= 129
- `aws_config_aggregation_authorization`= 130
- `aws_config_rule`= 131
- `aws_config_configuration_aggregator`= 132
- `aws_config_conformance_pack`= 133
- `aws_config_organization_config_rule`= 134
- `aws_config_organization_conformance_pack`= 135
- `aws_data_migration_service_endpoint`= 136
- `aws_data_migration_service_replication_instance`= 137
- `aws_data_migration_service_replication_task`= 138
- `aws_documentdb_dbcluster`= 139
- `aws_documentdb_dbinstance`= 140
- `aws_documentdb_globalcluster`= 141
- `aws_ecs_cluster`= 142
- `aws_ecs_service`= 143
- `aws_ecs_container_instance`= 144
- `aws_elasticache_cache_cluster`= 145
- `aws_elasticache_replication_group`= 146
- `aws_emr_cluster`= 147
- `aws_emr_notebook_execution`= 148
- `aws_emr_studio`= 149
- `aws_emr_instance`= 150
- `aws_fsx_association`= 151
- `aws_fsx_backup`= 152
- `aws_fsx_file_system`= 153
- `aws_fsx_storage_virtual_machine`= 154
- `aws_fsx_volume`= 155
- `aws_guard_duty_finding`= 156
- `aws_guard_duty_publishing_destination`= 157
- `aws_iam_user`= 158
- `aws_iam_group`= 159
- `aws_iam_role`= 160
- `aws_iam_policy`= 161
- `aws_iam_instance_profile`= 162
- `aws_ec2_image_builder_component_version`= 163
- `aws_ec2_image_builder_container_recipe`= 164
- `aws_ec2_image_builder_distribution_configuration`= 165
- `aws_ec2_image_builder_image_version`= 166
- `aws_ec2_image_builder_image_pipeline`= 167
- `aws_ec2_image_builder_image_recipe`= 168
- `aws_ec2_image_builder_infrastructure_configuration`= 169
- `aws_inspector_assessment_run`= 170
- `aws_inspector_finding`= 171
- `aws_lightsail_alarm`= 172
- `aws_lightsail_bucket`= 173
- `aws_lightsail_certificate`= 174
- `aws_lightsail_container_service`= 175
- `aws_lightsail_disk`= 176
- `aws_lightsail_distribution`= 177
- `aws_lightsail_domain`= 178
- `aws_lightsail_instance`= 179
- `aws_lightsail_key_pair`= 180
- `aws_lightsail_load_balancer`= 181
- `aws_lightsail_relational_database`= 182
- `aws_lightsail_static_ip`= 183
- `aws_memorydb_acls`= 184
- `aws_memorydb_cluster`= 185
- `aws_neptune_db_cluster_endpoint`= 186
- `aws_neptune_db_cluster`= 187
- `aws_neptune_db_instance`= 188
- `aws_neptune_global_cluster`= 189
- `aws_qldb_ledger`= 190
- `aws_qldb_stream`= 191
- `aws_rds_db_proxy`= 192
- `aws_rds_db_cluster`= 193
- `aws_rds_db_instance`= 194
- `aws_ram_resource`= 195
- `aws_ram_resource_share`= 196
- `aws_sagemaker_image`= 197
- `aws_sagemaker_endpoint`= 198
- `aws_sagemaker_domain`= 199
- `aws_sagemaker_code_repository`= 200
- `aws_sagemaker_work_team`= 201
- `aws_sagemaker_work_force`= 202
- `aws_sagemaker_notebook_instance`= 203
- `aws_sagemaker_model`= 204
- `aws_security_hub_product`= 205
- `aws_security_hub_standard`= 206
- `aws_security_hub_standard_control`= 207
- `aws_security_hub_insight`= 208
- `aws_simple_notification_service_topic`= 209
- `aws_simple_notification_service_platform_application`= 210
- `aws_subnet`= 211
- `aws_account`= 212
- `gcp_firewall`= 213
- `gcp_subnet`= 214
- `gcp_vpc`= 215
- `gcp_key_resource_management`= 216
- `gcp_account`= 217
- `gcp_security_group`= 218
- `gcp_iam_user`= 219
- `gcp_iam_role`= 220
- `gcp_iam_policy`= 221
- `user`= 222

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

### Bug Level-Specific Fields

#### Code Findings (bug_level = 1)
Access via `input.prefetched_code_bug`:
- file_name: Name of the file containing the vulnerability
- start_line_number: Starting line of vulnerable code
- end_line_number: Ending line of vulnerable code
- vulnerable_code: The actual vulnerable code snippet
- branch: Array of branch information

##### Web Findings (bug_level = 2)
Access via `input.prefetched_web_bug`:
- request: HTTP request details
- response: HTTP response details
- endpoints: List of affected endpoints (access URLs via endpoint.url)

##### Network Findings (bug_level = 4)
Access via `input.prefetched_network_bug`:
- port: Port information
- cpe: Common Platform Enumeration information

##### Package Findings (bug_level = 4,6)
Access via `input.prefetched_package_bug`:
- package_name: Name of the vulnerable package
- installed_version: Currently installed version
- fixed_version: Version that fixes the vulnerability
- branch: Array of branch information

##### Cloud Findings (bug_level = 5)
Access via `input.prefetched_cloud_bug`:
- region: Cloud region information
Based on cloud_type:
    ###### AWS (cloud_type = 2):
    - aws_resource_id: AWS Resource ID
    - aws_category: AWS Resource Category
    - aws_type: AWS Resource Type
    - vulnerable_id: AWS Account ID
    
    ###### Azure (cloud_type = 3):
    - azure_resource: Azure Resource ID
    - azure_category: Azure Resource Category
    
    ###### GCP (cloud_type = 4):
    - gcp_resource_id: GCP Resource ID
    - gcp_project_id: GCP Project ID
    - gcp_type: GCP Resource Type

### Prefetched Fields

#### prefetched_cve

- `id` (AutoField) - Primary key
- `title` (TextField) - Title of the CVE
- `description` (TextField) - Detailed description of the vulnerability
- `cvss_v2_data` (JSONField) - CVSS version 2 scoring data
- `cvss_v3_data` (JSONField) - CVSS version 3 scoring data
- `cvss` (FloatField) - CVSS score
- `cve_id` (CharField) - Unique CVE identifier
- `exploit_available` (BooleanField) - Flag indicating if exploit exists
- `exploit_info` (JSONField) - Detailed information about available exploits
- `patch_available` (BooleanField) - Flag indicating if patch exists
- `patch_info` (JSONField) - Detailed information about available patches
- `zero_day_available` (BooleanField) - Flag indicating if zero-day exists
- `is_wormable` (BooleanField) - Flag indicating if vulnerability is wormable
- `ti_raw_response` (JSONField) - Raw threat intelligence response
- `nvd_raw_response` (JSONField) - Raw NVD response
- `summary` (TextField) - Brief summary of the vulnerability
- `published` (DateTimeField) - Initial publication date
- `last_modified` (DateTimeField) - Last modification date
- `last_updated_nvd` (DateTimeField) - Last NVD update timestamp
- `last_updated_ti` (DateTimeField) - Last threat intelligence update timestamp
- `trend` (IntegerField) - Trend indicator
- `source` (CharField) - Source of the CVE information
- `advisories_seen` (ArrayField) - List of seen advisories
- `epss_score` (FloatField) - Exploit Prediction Scoring System score
- `cisa_due_date` (DateField) - CISA remediation due date
- `created` (DateTimeField) - Record creation timestamp
- `updated` (DateTimeField) - Record update timestamp

#### prefetched_cwe

- `id` (AutoField) - Primary key
- `cwe_id` (CharField) - Unique CWE identifier
- `type` (CharField) - Type of weakness
- `description` (TextField) - Detailed description of the weakness

#### prefetched_bug_tags

- `id` (AutoField) - Primary key
- `slug` (SlugField) - URL-friendly version of name
- `name` (CharField) - Tag name
- `created` (DateTimeField) - Creation timestamp
- `updated` (DateTimeField) - Update timestamp

#### prefetched_assigned_to

- `id` (AutoField) - Primary key
- `username` (CharField) - User's username
- `email` (EmailField) - User's email address
- `first_name` (CharField) - User's first name
- `last_name` (CharField) - User's last name

#### prefetched_bug_attachments

- `id` (AutoField) - Primary key
- `file` (FileField) - Attached file
- `name` (CharField) - Name of the attachment
- `created` (DateTimeField) - Creation timestamp

#### prefetched_engagements

- `id` (AutoField) - Primary key
- `name` (CharField) - Engagement name
- `description` (TextField) - Detailed description
- `start_date` (DateField) - Start date of engagement
- `end_date` (DateField) - End date of engagement

#### prefetched_nist

- `id` (AutoField) - Primary key
- `title` (CharField) - Control title
- `description` (TextField) - Detailed description
- `summary` (TextField) - Brief summary
- `nist_id` (CharField) - Unique NIST identifier
- `reference` (TextField) - Reference information
- `revision` (IntegerField) - Revision number

#### prefetched_owasp

- `id` (AutoField) - Primary key
- `title` (CharField) - Category title
- `year` (IntegerField) - Year of the OWASP category
- `label` (CharField) - Category label


## Accessing Custom Fields

Custom fields can be accessed using the `fields` attribute:

```python
def run_pipeline(input):
    custom_value = input.fields.get("custom_field_slug")
    return {"description": f"Custom field value: {custom_value}"}
```

Remember, the availability of some fields may depend on the context and configuration of your Strobes instance. Always test your pipelines thoroughly to ensure they work as expected with your data.
