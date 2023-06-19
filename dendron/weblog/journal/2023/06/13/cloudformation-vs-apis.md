---
id: y4qxeyd9iy3mnwag3dox9fc
title: Cloudformation Vs Apis
desc: ''
updated: 1686703213817
created: 1686702730467
topic: aws
tags: []
---

Some thoughts about infrastructure as code (IaC) build on top of cloudformation (eg. CDK, SAM) vs IaC build on top of APIs (eg. Terraform, Pulumi)

Note that this is NOT going into the merits of using a declarative DSL or a programming language to do IaC or even doing IaC outside of AWS - the following points are solely for evaluating the effectiveness of doing IaC with cloudformation at the base vs API calls. 

## cloudformation 

### pros
- lots of documentation
- best in class support for aws services
- built-in support for multi-region and multi-account deployments 

### cons
- generallly does not have day one support for new services 
- failed deployments are painful (cloudformation will try to rollback vs stoppig)
- can't import existing resources

## api 

### pros
- faster support for services that do not have cloudformation support
- ability to import existing resources

### cons
- requires contributors or vendor to keep api abstractions up to date
- more leaky abstractions and edge cases to keep in mind (eg. https://github.com/hashicorp/terraform-provider-aws/issues/10654)


