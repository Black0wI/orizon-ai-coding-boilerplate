# Directives

Directives are Standard Operating Procedures (SOPs) written in Markdown. They define **what** to do, not **how** to do it (that's for execution scripts).

## What Goes in a Directive

Each directive should contain:

| Section | Description |
|---------|-------------|
| **Goal** | What this directive accomplishes |
| **Inputs** | What the agent needs to start |
| **Tools/Scripts** | Which execution scripts to use |
| **Outputs** | What gets produced |
| **Edge Cases** | Known gotchas, rate limits, error handling |

## Creating a New Directive

1. Copy `_template.md` to a new file
2. Name it descriptively (e.g., `scrape_linkedin_profiles.md`)
3. Fill in all sections
4. Update as you learn (directives are living documents)

## Best Practices

- **Be specific**: Write instructions like you're explaining to a mid-level employee
- **Reference scripts**: Always point to specific files in `execution/`
- **Document learnings**: When errors happen, update the directive with what you learned
- **Keep it current**: Outdated directives cause failures
