# Backend for Frontends (BFFs)

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn src.main:app --host localhost --port 8003 --reload
```

### Correr docker-compose usando profiles
```bash
docker-compose --profile <pulsar|aeroalpes|ui|notificacion> up
```
