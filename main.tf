locals {
  regex_output = regex(
    file("${path.module}/domain_regex.txt"),
    var.dns_name
  )
}
