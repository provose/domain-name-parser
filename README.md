# Terraform Domain Parser

This is a Terraform module that breaks up a DNS name (like `www.google.co.uk`)
into parts. Currently we return:

- the domain (e.g. `google`)
- the suffix (e.g. `co.uk`)

## Usage

```terraform
# In Terraform, the module name can be whatever you want.
# Here, we go with "parser_1".

module "parser_1" {
  source   = "github.com/provose/domain-name-parser?ref=v1.0.0"
  dns_name = "a.bunch.of.com.subdomain.google.co.uk"
}

# You can access the domain with
# module.parser_1.domain

# and the suffix with
# module.parser_1.suffix
```
