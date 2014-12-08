# missingcloud

## Introduction

This project has a simple goal.  Collect cloud-related data you really
want and make it available in a format that you can use
programmatically.  Initially, this is focused on AWS-related stuff
like:

 * Available services
 * Available regions
 * Endpoints for each service in each region
 * Available instance types for EC2

This is all stuff that it seems should be available programmatically
but isn't.  So, until it is at least we can curate some JSON data
files that contain this information and provide access to it.

If there is other data you would find useful, let me know or just fork
the project and send a pull request.

## IP Ranges

The IP address ranges for each EC2 region were discovered using [this](https://gist.github.com/559397) and later maintained manually from the regularly 
announced [Amazon EC2 Public IP Ranges](https://forums.aws.amazon.com/ann.jspa?annID=1701).

* **NB**: The [AWS public IP address ranges are meanwhile programmatically available in JSON Form](http://aws.amazon.com/blogs/aws/aws-ip-ranges-json/) 
and the ranges still listed herein are not completely up to date anymore - this is currently dicussed in [issue #28](https://github.com/garnaat/missingcloud/issues/28).
