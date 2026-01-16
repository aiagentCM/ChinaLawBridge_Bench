ChinaLawBridge Bench: Evaluation Toolkit for Foreigners' Legal AI Agents
1. Objective
This project provides a specialized Automated Evaluation Benchmark designed for "China Law Expert" AI Agents. The primary goal is to assess an agent's capability to resolve fundamental legal requirements for foreigners in China across 5 critical dimensions:

Entry & Residence: Visa compliance, residence permits, and stay extensions.

Labor Rights: Employment contracts, social security obligations, and labor dispute resolution.

Commercial Interaction: Housing rentals, banking/payment services, and consumer protection.

Administrative Regulation: Temporary residence registration and individual income tax (IIT) compliance.

Dispute Resolution: Procedural guidance for foreign-related arbitration and litigation.

2. The Evaluation Toolkit Components
This toolkit is built for "end-to-end" testing with zero manual intervention, adhering to the "Green Agent" competition standards:

tasks.json (Benchmark Dataset): A curated set of 20 complex, multi-turn legal scenarios simulating real-world challenges faced by expats in China.

main.py (Evaluation Engine): An automated framework that loads the dataset, interacts with the target AI Agent, and logs evaluation results.

Dockerfile (Environment Image): A pre-configured execution environment ensuring that the evaluation is reproducible and consistent across any infrastructure.

3. How to Run the Evaluation (Build & Run)
Step 1: Build the Evaluation Environment
Run the following command in the root directory to build the "Evaluator" image:

Bash

docker build -t aiagentcm/chinalawbridge_bench:v1 .

Step 2: Execute the Automated Benchmark
Start the container to trigger the automated evaluation process. The system will automatically read tasks.json and execute main.py:

Bash

docker run -p 5000:5000 aiagentcm/chinalawbridge_bench:v1
4. Automation & "Green Agent" Compliance
Zero-Manual Setup: All dependencies, libraries, and the test dataset are baked into the Docker image.

Fully Autonomous: Upon container startup, the toolkit completes the entire workflow—from data ingestion to result output—without requiring external input or human prompts.
