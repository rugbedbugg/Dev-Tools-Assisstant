from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()

def main():
    workflow = Workflow()
    print("Developer Tools Research Agent")

    while True:
        query = input(">>> ").strip()[4:]
        if query.lower() in {"quit", "exit"}:
            break

        if query:
            result = workflow.run(query=query)
            print(f"\n📊📊 Results for: {query}")
            print("-"*60)

            for i, company in enumerate(result.companies, 1):
                print(f"\n🏢 {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Pricing: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   ⚒️ Tech Stack: {', '.join(company.tech_stack)}")
                else:
                    print(f"   ⚒️ Tech Stack: ❌ Not Available")

                if company.language_support:
                    print(f"   📜 Language Support: {', '.join(company.language_support)}")
                else:
                    print(f"   📜 Language Support: ❌ Not Available")

                if company.api_available:
                    print(f"   🔌 API: ✅ Available")
                else:
                    print(f"   🔌 API: ❌ Not Available")

                if company.integration_capabilities:
                    print(f"   🔗 Integrations: {', '.join(company.integration_capabilities)}")
                else:
                    print(f"   🔗 Integrations: ❌ Not Available")

                print()

            if result.analysis:
                print("Developer Recommendations: ")
                print("-"*40)
                print(result.analysis)


if __name__ == "__main__":
    main()
