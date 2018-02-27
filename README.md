# Cloudwatch Nomad metrics

Export the count of dead, pending and running Nomad jobs to Cloudwatch. The
script assumes it runs on a machine with a running localhost Nomad agent, and
has access to AWS credentials, be it through environment variables, shared
credentials file or EC2 instance role.

The script has no configuration capabilities but being very small it should be
quite easy to modify.

It exports to the following Cloudwatch metrics
( _Namespace/Name(dimension=value)_ ) :

 * Nomad/Job count(State=running)
 * Nomad/Job count(State=pending)
 * Nomad/Job count(State=dead)
