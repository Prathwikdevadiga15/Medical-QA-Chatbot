import time
from datetime import datetime

from knowledge_updater import update_knowledge_base


# =====================================================
# CONFIGURATION
# =====================================================

# Testing: update every 30 seconds
UPDATE_INTERVAL = 30

# For real deployment, you can use:
# UPDATE_INTERVAL = 3600
# This means every 1 hour.


# =====================================================
# SCHEDULER FUNCTION
# =====================================================

def run_scheduler():

    print("=" * 60)

    print(
        "🩺 Dynamic Medical Knowledge Base Scheduler"
    )

    print("=" * 60)

    print(
        f"Update interval: "
        f"{UPDATE_INTERVAL} seconds"
    )

    print(
        "\nScheduler started successfully."
    )


    while True:

        print("\n" + "-" * 60)

        print(
            f"Checking knowledge base..."
        )

        print(
            f"Time: {datetime.now()}"
        )

        try:

            # Run the knowledge-base update
            update_knowledge_base()

            print(
                "\n✅ Knowledge base update completed successfully."
            )

        except Exception as error:

            print(
                "\n❌ Knowledge base update failed:"
            )

            print(
                error
            )


        print(
            f"\n⏳ Next update in "
            f"{UPDATE_INTERVAL} seconds..."
        )


        # Wait before checking again
        time.sleep(
            UPDATE_INTERVAL
        )


# =====================================================
# START SCHEDULER
# =====================================================

if __name__ == "__main__":

    try:

        run_scheduler()

    except KeyboardInterrupt:

        print(
            "\n\n🛑 Scheduler stopped by user."
        )