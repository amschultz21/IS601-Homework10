# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

🔗 Closed GitHub Issues

Username validation fails for special characters and short nicknames

Password schema allows weak passwords (missing uppercase, etc.)

Test coverage missing for invalid password formats

Edge cases for profile updates not fully tested

URL validation missing for profile fields

All issues include accompanying tests and code changes merged to the main branch.

🐳 DockerHub Link

View the deployed image: https://hub.docker.com/r/amschultz21/is601-homework10

✅ Achieved 100% test coverage using pytest and pytest-cov.
Unit tests cover schema validation, edge cases, error handling, and success paths for user-related API endpoints.

🧠 Reflection

This assignment gave me hands-on experience applying real-world validation and testing practices within a full-stack web application. From a technical perspective, I improved form validation logic using Pydantic schemas and schema-level validators, ensuring secure and user-friendly input handling for fields like password, nickname, and profile URLs. I also explored how to handle edge cases gracefully, and added unit tests that simulate real user behaviors — from submitting broken URLs to updating only one field in a profile form.

On the collaborative side, I gained confidence in using GitHub Issues to track progress and make each fix traceable. Documenting and closing each issue helped me organize my development process more clearly. Managing commits, pushing test-driven fixes, and reflecting on peer review practices improved my understanding of how clean development workflows function in a team environment. Overall, this project helped reinforce good habits around validation, testing, and version control that will carry into future API and full-stack projects.