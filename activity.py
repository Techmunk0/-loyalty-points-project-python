from dataclasses import dataclass

from temporalio import activity


@dataclass
class Email:
    to: str
    subject: str
    body: str


@activity.defn
async def send_email(details: Email) -> str:
    print(
        f"Sending email to {details.to} with subject {details.subject} and body {details.body}"
    )
    return "success"
