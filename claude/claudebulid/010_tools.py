# Load env variables and create client
from pyexpat.errors import messages
from urllib import response

from urllib import response

from dotenv import load_dotenv
from anthropic import Anthropic
from datetime import datetime, timedelta
from anthropic.types import ToolParam, Message

from datetime import datetime, timedelta
import json


load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"

# Helper functions
def add_user_message(messages, message):
    user_message = {
        "role": "user", 
        "content": message.content if isinstance(message, Message) else message}
    messages.append(user_message)


def add_assistant_message(messages, message):
    assistant_message = {
        "role": "assistant", 
        "content": message.content if isinstance(message, Message) else message}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message


def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )


# Tools and Schemas
def add_duration_to_datetime(
    datetime_str, duration=0, unit="days", input_format="%Y-%m-%d"
):
    date = datetime.strptime(datetime_str, input_format)

    if unit == "seconds":
        new_date = date + timedelta(seconds=duration)
    elif unit == "minutes":
        new_date = date + timedelta(minutes=duration)
    elif unit == "hours":
        new_date = date + timedelta(hours=duration)
    elif unit == "days":
        new_date = date + timedelta(days=duration)
    elif unit == "weeks":
        new_date = date + timedelta(weeks=duration)
    elif unit == "months":
        month = date.month + duration
        year = date.year + month // 12
        month = month % 12
        if month == 0:
            month = 12
            year -= 1
        day = min(
            date.day,
            [
                31,
                29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31,
            ][month - 1],
        )
        new_date = date.replace(year=year, month=month, day=day)
    elif unit == "years":
        new_date = date.replace(year=date.year + duration)
    else:
        raise ValueError(f"Unsupported time unit: {unit}")

    return new_date.strftime("%A, %B %d, %Y %I:%M:%S %p")


def set_reminder(content, timestamp):
    print(f"----\nSetting the following reminder for {timestamp}:\n{content}\n----")


add_duration_to_datetime_schema = {
    "name": "add_duration_to_datetime",
    "description": "Adds a specified duration to a datetime string and returns the resulting datetime in a detailed format. This tool converts an input datetime string to a Python datetime object, adds the specified duration in the requested unit, and returns a formatted string of the resulting datetime. It handles various time units including seconds, minutes, hours, days, weeks, months, and years, with special handling for month and year calculations to account for varying month lengths and leap years. The output is always returned in a detailed format that includes the day of the week, month name, day, year, and time with AM/PM indicator (e.g., 'Thursday, April 03, 2025 10:30:00 AM').",
    "input_schema": {
        "type": "object",
        "properties": {
            "datetime_str": {
                "type": "string",
                "description": "The input datetime string to which the duration will be added. This should be formatted according to the input_format parameter.",
            },
            "duration": {
                "type": "number",
                "description": "The amount of time to add to the datetime. Can be positive (for future dates) or negative (for past dates). Defaults to 0.",
            },
            "unit": {
                "type": "string",
                "description": "The unit of time for the duration. Must be one of: 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', or 'years'. Defaults to 'days'.",
            },
            "input_format": {
                "type": "string",
                "description": "The format string for parsing the input datetime_str, using Python's strptime format codes. For example, '%Y-%m-%d' for ISO format dates like '2025-04-03'. Defaults to '%Y-%m-%d'.",
            },
        },
        "required": ["datetime_str"],
    },
}

set_reminder_schema = {
    "name": "set_reminder",
    "description": "Creates a timed reminder that will notify the user at the specified time with the provided content. This tool schedules a notification to be delivered to the user at the exact timestamp provided. It should be used when a user wants to be reminded about something specific at a future point in time. The reminder system will store the content and timestamp, then trigger a notification through the user's preferred notification channels (mobile alerts, email, etc.) when the specified time arrives. Reminders are persisted even if the application is closed or the device is restarted. Users can rely on this function for important time-sensitive notifications such as meetings, tasks, medication schedules, or any other time-bound activities.",
    "input_schema": {
        "type": "object",
        "properties": {
            "content": {
                "type": "string",
                "description": "The message text that will be displayed in the reminder notification. This should contain the specific information the user wants to be reminded about, such as 'Take medication', 'Join video call with team', or 'Pay utility bills'.",
            },
            "timestamp": {
                "type": "string",
                "description": "The exact date and time when the reminder should be triggered, formatted as an ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SS) or a Unix timestamp. The system handles all timezone processing internally, ensuring reminders are triggered at the correct time regardless of where the user is located. Users can simply specify the desired time without worrying about timezone configurations.",
            },
        },
        "required": ["content", "timestamp"],
    },
}

batch_tool_schema = {
    "name": "batch_tool",
    "description": "Invoke multiple other tool calls simultaneously",
    "input_schema": {
        "type": "object",
        "properties": {
            "invocations": {
                "type": "array",
                "description": "The tool calls to invoke",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the tool to invoke",
                        },
                        "arguments": {
                            "type": "string",
                            "description": "The arguments to the tool, encoded as a JSON string",
                        },
                    },
                    "required": ["name", "arguments"],
                },
            }
        },
        "required": ["invocations"],
    },
}


#pass
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
       raise ValueError("Date format cannot be empty.")
    return datetime.now().strftime(date_format)

def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


def run_tools(message):
    tool_requests = [
        block for block in message.content if block.type == "tool_use"
    ]
     
    tool_result_blocks = []

    for tool_request in tool_requests:
        try:
            tool_output = run_tool(tool_request.name, tool_request.input)
            tool_result_block = {
                    "type": "tool_result",
                    "content": json.dumps(tool_output),
                    "tool_use_id": tool_request.id,
                    "is_error": False
            }
        except Exception as e:
            tool_result_block = {
                    "type": "tool_result",
                    "content": f"Error executing tool: {str(e)}",
                    "tool_use_id": tool_request.id,
                    "is_error": True
            }

        tool_result_blocks.append(tool_result_block)
    return tool_result_blocks
        
def run_conversation(messages):

    while True:
        response = chat(messages, tools=[
            get_current_datetime_schema,
            add_duration_to_datetime_schema,
            set_reminder_schema,])
        print("00000000000000 - Response Received :  "+ str(response))
        add_assistant_message(messages, response)
        print("11111111111111")
        print(text_from_message(response))
    
        if response.stop_reason != "tool_use":
            break

        tool_results = run_tools(response)
        #print("22222222222222  :  "+ str(tool_results))
        add_user_message(messages, tool_results)
 
    return messages



get_current_datetime_schema = ToolParam({
  "name": "get_current_datetime",
  "description": "Returns the current date and time formatted as a string. Use this tool whenever the user asks for the current date, time, or both. The format follows Python's strftime directives (e.g., '%Y-%m-%d' for date only, '%H:%M:%S' for time only).",
  "input_schema": {
    "type": "object",
    "properties": {
      "date_format": {
        "type": "string",
        "description": "A strftime-compatible format string that controls the output. Defaults to '%Y-%m-%d %H:%M:%S'. Must not be empty. Examples: '%Y-%m-%d' for date only, '%H:%M:%S' for time only, '%d/%m/%Y %I:%M %p' for 12-hour format with day/month/year."
      }
    },
    "required": []
  }
})


def main() -> None:
    #get_current_datetime("%H:%M");
    messages = []

    """ messages.append( 
        {
            "role": "user",
            "content": "What is the exact time, formatted as HH:MM:SS?"
        }
    )

    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        tools=[get_current_datetime_schema],
    )
    messages.append({"role": "assistant", "content": response.content})

    result= get_current_datetime(**response.content[0].input)

    messages.append({
        "role": "user",
        "content": [{
            "type": "tool_result",
            "tool_use_id": response.content[0].id,
            "content": result,
            "is_error": False
        }]
    })

   # print(messages)

    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        tools=[get_current_datetime_schema],
    )

    add_assistant_message(messages, response.content)
 """
    
    add_user_message(messages, "set a reminder for my doctor appointment. it after 3 days from now at 3 PM")
    run_conversation(messages)
    print(messages)



    
if __name__ == "__main__":
    main()