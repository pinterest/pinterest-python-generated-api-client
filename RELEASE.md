
## Release Process

### GitHub

[Releases](https://github.com/pinterest/pinterest-python-generated-api-client/releases) are published
to our [pinterest-python-generated-api-client][] open source project.

#### Setup

1. Become an [open source contributor][] and contact a GitHub admin to get
   added as maintainers to the [`Pinterest Python Generated API Client`](https://github.com/pinterest/pinterest-python-generated-api-client) team.
2. Check out a local copy of the (public) [pinterest/pinterest-python-generated-api-client][https://github.com/pinterest/pinterest-python-generated-api-client] repository.


#### Release

1. Go to you local version of `pinterest/pinterest-python-generated-api-client` change the `spec/config.yml#packageVersion`
   
2. Run the following command 
   ```shell
   cd spec
   make 
   ```

3. Open a new Pull Request with those changes to the [pinterest/pinterest-python-generated-api-client][]
   project. The PR branch must follow this format `release/<version>` with the release note in the PR description 

4. Get that Pull Request reviewed and merged to `main`, and then pull the
   updated `main` branch files to your local copy.

5. Tag the release (use the same version in the `spec/config.yml#packageVersion` file):
   
   ```shell
   git tag $VERSION
   ```

6. Push that tag to the repository.
   
   ```shell
   git push --tags
   ```

7. [Create a release](https://github.com/pinterest/pinterest-python-generated-api-client/releases/new)
   for your new tag and include the version's release notes in the description (use the same release PR description).


[pinterest/pinterest-python-generated-api-client]: https://github.com/pinterest/pinterest-python-generated-api-client
