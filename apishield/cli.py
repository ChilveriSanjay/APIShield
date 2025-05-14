# api_security_checker/cli.py
import click
from decorators import apishield

@click.group()
def cli():
    """# 🚀🚀 Welcome to the APIShield ! 🚀🚀
    AI Agent for API Security & Documentation"""
    pass

@click.command()
@click.argument("view_func_name")
def review(view_func_name):

    print(apishield(view_func_name))

if __name__ == '__main__':
    cli()
