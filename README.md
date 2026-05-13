A small example repo to create bug report for https://github.com/schemathesis/schemathesis

### How to run

Running api:

```zsh
python3 -m venv venv
source venv/bin/activate
pip install "fastapi[standard]"
fastapi dev
```

Running schemathesis:

```zsh
SCHEMATHESIS_HOOKS="./hook.py" schemathesis --config-file ./schemathesis.toml run ./oas.yaml --url http://127.0.0.1:8000 --wait-for-schema 60 --report junit
```

Bug which occurs:

```
=================================== FAILURES ===================================
__________________________________ GET /point __________________________________
1. Test Case ID: Odqtsk

- API accepted schema-violating request

    Invalid data should have been rejected
    Expected: 400, 401, 403, 404, 405, 406, 422, 428, 5xx
    Invalid component: in query - all required and 3 optional properties

[200] OK:

    `[{"type":"type2","id":"id2","name":"name2","lat":0.0,"lon":0.0,"asl":null,"distanceKm":0.0}]`

Reproduce with:

    curl -X GET 'http://127.0.0.1:8000/point?lat=0&lon=0&asl=0.0&maxHeightDiff=1.0&maxDistance=100.0'
```

### Description:

- It seems when a hook is used, even if it does mostly nothing it somehow breaks something
- The request which supposedly violates the schema doesn't actually violate the schema
