## Start a Workflow

```command
# terminal one
poetry run python app.py
# terminal two
poetry run python main.py
```

## Example commands

```bash
curl -X POST http://localhost:5000/123
curl -X POST http://localhost:5000/123/add_points/100
curl -X POST http://localhost:5000/123/add_points/30
curl -X POST http://localhost:5000/123/add_points/20
curl -X GET http://localhost:5000/123
```

## Get Points

```bash
curl -X GET http://localhost:5000/123
```

## Add points

```bash
curl -X POST http://localhost:5000/123/add_points/850
```

## Spend points

```bash
curl -X POST http://localhost:5000/123/spend_points/10
```

## End Workflow

```bash
curl -X DELETE http://localhost:5000/123/exit
```

## Terminate

```bash
temporal workflow terminate --workflow-id 123
```

## Reset

Execute Batch Reset command:

```bash
temporal workflow reset-batch --query "WorkflowType='LoyaltyProgram'" --reason "Sev2: id.1259" --type LastWorkflowTask
```

Dry run a Batch Reset command:

```bash
temporal workflow reset-batch --query "WorkflowType='LoyaltyProgram'" --reason "Sev2: id.1259" --type LastWorkflowTask --dry-run
```
