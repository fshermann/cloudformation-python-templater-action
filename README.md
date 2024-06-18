# CloudFormation Python Template Generator
This action is intended to simplify some niche problems in github actions based deployments of Cloudformation stacks. 

In its simplest form, this is functionally just adding a "rendering" step that is ultimately deployed. This action bundles in the SAM deployment as well since many of the use cases require us to have context of the runtime environment.

# Contrived Example Use Case
Assume I have a cloudformation template with resources like so:
```yaml
Resources:
    Type: AWS::S3::Bucket
    Properties:
        BucketName: !Ref "AWS::StackName"
```

If the stack name contains invalid characters or is too long, there is no simple way to handle this in native cloudformation. In python we could do something simple like:
```python
# ensure all characters are lowercase and only take 64 characters
stack_name.lower()[:64]
```

This wrapper introduces a way to perform basic data manipulation on cloudformation templates.

# Why??
At my day job we use SAM to deploy many applications. There are many limitations to CloudFormation that makes it difficult to use. The syntax for CloudFormation intrinsic functions is very ugly and foreign to many people. There are also many obvious pieces of functionality missing.

The obvious alternative to this is CDK. While CDK does fix many of the limitations, it has a fairly steep learning curve and changes the deployment tools.

# Limitations
1. All attributes you wish to modify using this tool must be available elsewhere in the template. It cannot be used on anything determined at execution time.

# TODO/Problems
1. Write class to parse JSONified YAML
2. Figure out how to handle Refs to other resources (maybe we just do `.` syntax?)
   1. Validation that the property exists
3. Write some basic processing/util functions
   1. String
      1. split
      2. upper
      3. lower
      4. replace
      5. strip
      6. join
      7. zfill
      8. truncate
   2. Generic
      1. get_timestamp
      2. get_uuid
4. Handle conditionals
5. Handle iteration
6. Allow custom function hooks that can output YAML