"""Tokenizing and Parsing - Part I"""
import requests


def tokenizer(target, prefix, suffix: str = "\n"):
    """function to generate tokens"""
    list_of_content = target.split()
    if prefix == "href":
        list_of_tokens = [i for i in list_of_content if prefix in i]
    else:
        for i in list_of_content:
            list_of_tokens = [
                i
                for i in list_of_content
                if (i[0 : len(prefix)] == prefix) and (i[-(len(suffix)) :] == suffix)
            ]
    return list_of_tokens


def get_url_list(input_url: str = "https://httpbin.org"):
    """function to find urls"""
    total_urls = []
    get_object = requests.get(input_url, timeout=1)
    temp_urls = tokenizer(get_object.text, "href", ">")
    for url in temp_urls:
        start_index = url.find("http")
        temp = url[start_index:]
        end_index = temp.find('"')
        temp_url = url[start_index:end_index]
        if temp_url:
            total_urls.append(temp_url)
    return total_urls


def infix_to_postfix(infix_expression: str):
    """function to convert infix expresion to postfix"""
    precedence_dict = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
    ans = []
    stack_list = []
    for i in infix_expression:
        if i == " ":
            continue
        if i.lower() >= "a" and i.lower() <= "z":
            ans.append(i)
        else:
            if i == "(":
                stack_list.append(i)
            elif i == ")":
                while stack_list and stack_list[-1] != "(":
                    ans.append(stack_list.pop())
                stack_list.pop()
            elif not stack_list or stack_list[-1] == "(":
                stack_list.append(i)
            elif stack_list[-1] == "^" and i == "^":
                stack_list.append(i)
            elif precedence_dict[stack_list[-1]] < precedence_dict[i]:
                stack_list.append(i)
            else:
                while (
                    stack_list
                    and stack_list[-1] != "("
                    and precedence_dict[stack_list[-1]] >= precedence_dict[i]
                ):
                    ans.append(stack_list[-1])
                    stack_list.pop()
                stack_list.append(i)
    while stack_list:
        ans.append(stack_list.pop())
    return ans


if __name__ == "__main__":
    print(get_url_list())
    print(tokenizer("My name is Mango Akash.", "M", "go"))
    print(infix_to_postfix("(a + b) ^ c - d / q"))
