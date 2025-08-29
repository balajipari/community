#!/usr/bin/env python3
import click
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from ai_client import AIClient

console = Console()

@click.command()
@click.option('--model', '-m', default='auto', help='AI model to use (openai, ollama, auto)')
@click.option('--reset', '-r', is_flag=True, help='Reset conversation history')
def main(model, reset):
    """Ideation Buddy CLI - AI-powered product ideation assistant"""
    
    console.print(Panel.fit(
        "[bold blue]🚀 Ideation Buddy CLI[/bold blue]\n"
        "[dim]Your AI-powered product ideation assistant[/dim]",
        border_style="blue"
    ))
    
    # Initialize AI client
    ai_client = AIClient()
    
    if reset:
        ai_client.reset_conversation()
        console.print("[green]Conversation history reset![/green]")
    
    # Set model preference
    if model == 'ollama':
        ai_client.config.USE_OLLAMA = True
        console.print("[yellow]Using Ollama model[/yellow]")
    elif model == 'openai':
        ai_client.config.USE_OLLAMA = False
        console.print("[yellow]Using OpenAI model[/yellow]")
    else:
        console.print("[yellow]Auto-detecting AI service...[/yellow]")
    
    console.print("\n[bold]Starting ideation session...[/bold]")
    console.print("Type 'quit' or 'exit' to end the session\n")
    
    # Start the conversation
    try:
        while True:
            # Get user input
            user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                console.print("\n[green]Thank you for using Ideation Buddy![/green]")
                break
            
            if not user_input.strip():
                continue
            
            # Show thinking indicator
            with console.status("[bold yellow]Thinking..."):
                response = ai_client.get_response(user_input)
            
            # Display AI response
            console.print("\n[bold green]AI Assistant[/bold green]")
            
            # Try to parse JSON response for better formatting
            try:
                parsed_response = json.loads(response)
                if parsed_response.get('type') == 'completion':
                    # Show completion summary
                    content = parsed_response['content']
                    console.print(Panel(
                        f"[bold green]🎉 Ideation Complete![/bold green]\n\n"
                        f"[bold]Motto:[/bold] {content.get('motto', 'N/A')}\n"
                        f"[bold]Problem:[/bold] {content.get('problem_statement', 'N/A')}\n"
                        f"[bold]Target Users:[/bold] {content.get('target_users', 'N/A')}\n"
                        f"[bold]ICP:[/bold] {content.get('ICP', 'N/A')}\n"
                        f"[bold]Value Prop:[/bold] {content.get('value_prop', 'N/A')}\n"
                        f"[bold]Alternatives:[/bold] {content.get('alternatives', 'N/A')}",
                        border_style="green"
                    ))
                else:
                    # Show regular response
                    console.print(response)
            except json.JSONDecodeError:
                # Not JSON, display as regular text
                console.print(response)
            
            console.print()  # Empty line for spacing
    
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Session interrupted. Goodbye![/yellow]")
    except Exception as e:
        console.print(f"\n[red]An error occurred: {e}[/red]")

if __name__ == '__main__':
    main()
