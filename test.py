from openai import OpenAI
client = OpenAI(
    api_key = "" #openAI key here
)

mail = """
Subject: Project Update and Next Steps

From: heiko@example.com
To: team@example.com
Date: September 17, 2025

Dear Team,

I hope this message finds you well. I wanted to take a moment to provide an update on our current project and outline the next steps as we move forward.

As of today, we have successfully completed the initial phases of the project, including the research and development stages. The feedback we received from our initial testing has been overwhelmingly positive, and I want to thank each of you for your hard work and dedication. Your efforts have truly made a difference in getting us to this point.

Looking ahead, we will be entering the implementation phase next week. I would like to schedule a meeting on September 20, 2025, to discuss our strategies and ensure that everyone is aligned on their responsibilities. Please let me know your availability for that day, and I will do my best to accommodate everyone.

Additionally, I encourage you to review the project timeline and deliverables outlined in our shared document. If you have any questions or concerns, please do not hesitate to reach out. Open communication is key to our success, and I want to ensure that everyone feels supported throughout this process.

Lastly, I would like to remind everyone to keep an eye on our project management tool for updates and tasks assigned to you. Your contributions are invaluable, and I appreciate your commitment to making this project a success.

Thank you once again for your hard work. I look forward to our continued collaboration and achieving great results together.

Best regards,

Heiko Müller
Project Manager
heiko@example.com
+49 123 456 7890


"""
# https://platform.openai.com/docs/pricing
def summarize(mail):
    response = client.responses.create(
        model="gpt-5-mini",
        input=mail
    )
    return(response.output_text)
    
def mail_response(mail, style):
    prompt = f"antworte auf die mail in folgendem Stil:{style}\n"
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt + mail
    )
    return(response.output_text)

