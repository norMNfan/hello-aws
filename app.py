import json
import math

def lambda_handler(event, context):
    try:
        # BUG 1: Misspelled 'param' name ('a' is required, but code looks for 'alpha')
        a = float(event["a"])  # corrected from 'alpha' to 'a'
        b = float(event["b"])
        c = float(event["c"])

        # BUG 2: No check for division by zero when 'a' is zero
        if a == 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Parameter 'a' cannot be zero."})
            }

        discriminant = b**2 - 4*a*c

        # BUG 3: Incorrectly checking for discriminant using assignment instead of comparison
        if discriminant == 0:  # corrected from '=' to '=='
            root = -b / (2*a)
            return {
                "statusCode": 200,
                "body": json.dumps({"root": root})
            }

        if discriminant < 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No real roots"})
            }

        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)

        return {
            "statusCode": 200,
            "body": json.dumps({"root1": root1, "root2": root2})
        }

    except KeyError as e:
        # BUG 4: Not formatting the exception string properly
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing parameter: " + str(e)})  # corrected to use str(e)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Unexpected error: {str(e)}"})
        }