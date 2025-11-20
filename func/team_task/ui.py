import discord
from .model import Task

def task_to_embed(task: Task) -> discord.Embed:
    color = (
        discord.Color.gold() if task.status == "pending" else
        discord.Color.blue() if task.status == "in_progress" else
        discord.Color.green()
    )

    embed = discord.Embed(
        title=f"📌 Task #{task.task_id}: {task.title}",
        description=task.description or "No description.",
        color=color
    )

    embed.add_field(name="👤 Assigned to", value=task.assigned_to or "Unassigned", inline=False)
    embed.add_field(name="📅 Created", value=task.created_at, inline=False)
    embed.add_field(name="🔧 Status", value=task.status, inline=False)

    return embed
