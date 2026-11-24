from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from openai.types.responses import response_prompt

load_dotenv()


def main():
    print("Hello from langchain-demo!")
    # print(os.environ.get("OPENAI_API_KEY"))
    information = """
    Amazon.com, Inc.[1] (doing business as Amazon)[a] is an American multinational conglomerate engaged in e-commerce, retail, cloud computing, online advertising, digital streaming, entertainment, supermarkets, and artificial intelligence.[5] Founded in 1994 by Jeff Bezos in Bellevue, Washington,[6] the company started as an online book marketplace that gradually expanded to include virtually all consumer products as well as many other categories, positioned as "The Everything Store".[7]
    As of 2026, it was the world's biggest online retailer. Amazon sells books, electronics, pharmaceuticals, car parts, video games, dining products, jewelry, food, music, and sports equipment.[8]
    The company has multiple subsidiaries, including Amazon Web Services (AWS), which provides cloud computing; Zoox, a self-driving car division; satellite Internet provider Kuiper Systems; and Amazon Lab126, a computer hardware R&D provider. Other subsidiaries include Ring, Twitch, IMDb, and grocer Whole Foods Market. Amazon distributes downloadable and streaming content through its Amazon Prime Video, MGM+, Amazon Music, Twitch, Audible, and Wondery[9] units through its Entertainment division. It publishes books through its publishing arm, Amazon Publishing; produces and distributes film and television content through Amazon MGM Studios, including the Metro-Goldwyn-Mayer studio; and owns Brilliance Audio and Audible, which produce and distribute audiobooks, respectively. Amazon produces consumer electronics, most notably Kindle e-readers, Echo devices, Fire tablets, and Fire TVs.
    """

    summary_template = f"""
    given the information {information} about a company, I want you to create :
    1. A short summary
    2. two interseting facts about it.
    """
    summary_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template)
    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_template | llm
    response_prompt = chain.invoke(input={"information": information})
    print(response_prompt.content)


if __name__ == "__main__":
    main()
