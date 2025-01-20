---
id: rgyttdp613q8iewipo5n9lr
title: Migrating from Webflow to S3
desc: ''
updated: 1737175897228
created: 1737175897228
---

Its 2025. Some things change. Publishing a static site on S3 remains as byzantine as setting up salesforce.

In an ideal world, you'd be able to upload content to s3 and toggle an option to support serving static content. Maybe an extra toggle to support custom domains.

And this is kind of true. S3 has [website endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteEndpoints.html) to facilitate this usecsae.

But in order to use website endpoints, you first have to disable the public access block that comes default on all newly created s3 buckets (the consequence of one too many s3 bucket misconfigurations by fill in your blank large S&B 500 company). Then you have to add a bucket policy that allows public GET requests to the bucket. Then you enable it as a website endpoint.

Unfortunately, website endpoints do not support `https` which makes it dead on arrival for most use cases as both google bot and chrome will punish you for not having ssl certs.

In order to support ssl certs, you'll need to create a cloudfront distribution that redirects traffic to your your s3 bucket. If you're using a custom domain, you'll also need to register the cert with cloudfront and point your custom domain to said cloudfront distribution.

AWS created an [entirely new service](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) in order to stitch together these disparate steps.

I ended up creating [two bash scripts](https://github.com/kevinslin/static-s3-cloudfront-site/tree/main) to do most of the same thing with a little help from a [friend](https://openai.com/o1/).

This usecase and subsequent post was inspired by the need to migrate two static sites from webflow to anything else. Monthly hosting went down from $60/month to <$1/mo :)
