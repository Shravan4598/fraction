# Security Policy

Thank you for helping keep **Fraction** secure.

We take the security of this project seriously and appreciate responsible disclosure of potential vulnerabilities.

---

# Supported Versions

The following table indicates which versions currently receive security updates.

| Version | Supported |
| ------- | --------- |
| 1.x     | ✅ Yes     |
| 0.x     | ❌ No      |

Only the latest stable release receives security updates.

---

# Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub Issues.**

Instead, report them privately by contacting the project maintainer.

Recommended information to include:

* A clear description of the vulnerability
* Steps to reproduce the issue
* Expected behaviour
* Actual behaviour
* Proof of concept (if applicable)
* Affected package version
* Python version
* Operating system
* Any suggested mitigation or fix

Providing as much detail as possible helps us investigate and resolve the issue efficiently.

---

# What to Expect

After receiving a report, we aim to:

| Stage                       | Target Time                    |
| --------------------------- | ------------------------------ |
| Acknowledge receipt         | Within 48 hours                |
| Initial assessment          | Within 7 days                  |
| Status update               | Within 14 days                 |
| Security fix (if confirmed) | As soon as reasonably possible |

These timelines are goals rather than guarantees and may vary depending on the complexity of the issue.

---

# Coordinated Disclosure

We kindly ask that you:

* Allow reasonable time for investigation.
* Avoid publicly disclosing the vulnerability until a fix has been released.
* Work with the maintainers to coordinate responsible disclosure.

Responsible disclosure helps protect all users of the project.

---

# Scope

Examples of security-related issues include:

* Code execution vulnerabilities
* Dependency vulnerabilities
* Unsafe deserialization
* Supply-chain attacks
* Packaging vulnerabilities
* Build pipeline vulnerabilities
* CI/CD credential exposure
* Release integrity issues

Issues such as incorrect mathematical results, API enhancements, feature requests, or documentation mistakes are generally **not** considered security vulnerabilities unless they create a genuine security risk.

---

# Security Best Practices for Users

To help keep your applications secure:

* Always use the latest stable release.
* Keep Python up to date.
* Regularly update project dependencies.
* Verify packages are installed from trusted sources such as PyPI.
* Review release notes before upgrading.
* Run your own test suite after updating dependencies.

---

# Dependency Management

The project follows these practices:

* Uses modern Python packaging standards (PEP 517, PEP 518, and PEP 621).
* Tracks dependency updates regularly.
* Builds reproducible distribution artifacts.
* Uses automated CI to validate builds and tests before release.

---

# Release Security

Before every release, maintainers should:

1. Run the complete test suite.
2. Run static analysis and linting.
3. Build the source distribution and wheel.
4. Verify package metadata.
5. Validate generated artifacts.
6. Publish only verified release artifacts.

---

# Security Updates

Security fixes will be released as patch versions whenever possible.

Examples:

* 1.0.0 → 1.0.1
* 1.2.3 → 1.2.4

If a breaking change is required to resolve a severe issue, it will be documented clearly in the release notes and changelog.

---

# Third-Party Dependencies

Although **Fraction** has no required runtime dependencies, development tools and documentation packages should be kept up to date to reduce supply-chain risk.

Contributors are encouraged to:

* Monitor dependency advisories.
* Update development dependencies regularly.
* Avoid introducing unnecessary third-party packages.

---

# Acknowledgements

We sincerely thank security researchers and community members who responsibly report vulnerabilities and help improve the safety and reliability of this project.

Your efforts are greatly appreciated.
