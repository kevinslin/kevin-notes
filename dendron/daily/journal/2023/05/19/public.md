---
id: bcyoh1ruh5b570m9vlhvgf9
title: Public
desc: ''
updated: 1684557434196
created: 1684545450170
htag: journal
tags:
  - gpt
---

Been working with GPT to classify AWS service links and running into some issues with hallucinations. 

The problem statement: given an AWS service and a repository of github links, match the github link to the correct AWS Service. 

I was doing this in order to scrape all the AWS git repositories in order to consolidate and organize notable sections in [AWS Reference Notes](https://awsnotes.dendron.so/about/readme).

Service names were taken directly from the AWS notes. Sample below
```txt
AWS CodeStar
AWS Mobile SDK for Xamarin
...
```

AWS Github repos were scraped from the https://github.com/awsdocs page using the github API. Sample below
```txt
https://github.com/awsdocs/aws-codestar-user-guide.git
https://github.com/awsdocs/aws-xamarin-developer-guide.git
...
```

While most services could be mapped using rules by converting the aws service to kebab case, there were enough exceptions to this case (eg. aws mobile sdk for xamarian -> `aws-xamarin-developer-guide.git`) that I opted to grab the giant hammer that is the LLM (granted, it didn't take much). 

My prompt for GPT:
```py
output_format = """
[{
  "name": "Amazon EC2",
  "git_repo": "amazon-ec2-user-guide.git"
},
...
]
"""

system_message = SystemMessage(content=f"You match aws service names to their corresponding git repositories. You will be given a list of AWS services as one list and a list of git repositories as another list. Your job is to output a json list that matches the aws service name to the git repository.\n Example output format:\n'''{output_format}'''\nOnly match against the git repositories in the context. If you do not find a match, return NO_MATCH_FOUND")
human_message_prompt = HumanMessagePromptTemplate.from_template("AWS Repo List:\n'''\n{repo_list_string}\n'''\n\nAWS Service List:\n'''\n{service_names_string}\n'''\n\nOutput:")
chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message_prompt])
```

The syntax here is written from [langchain](en.wikipedia.org/wiki/LangChain), a popular open source software framework for applying LLMs. 
The system prompt tells GPT to match service names to git repositories. The two sentences at the end are a first layer guard against hallucinations, asking GPT to only use the given context and have a escape clause (`NO_MATCH_FOUND`) if it is unsure. Without this guard, GPT would otherwise generate matches for ALL services and make up git repository urls. 

The human prompt feeds in the available AWS git repositories as well as the services. To make this prompt fit the content length, I divide the AWS service list into chunks of 15 elements each. Running this, GPT was able to match links for 76/106 services. 

I then further filtered the results as I had a source of truth (the actual list of valid git repositories). Running this filter, I ended up with 39/106 services. 

In this particular use case, dealing with hallucinations is manageable because we have a source of truth and an easy way to verify. In many cases, its not as clear cut. 
