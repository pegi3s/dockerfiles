from unipressed.id_mapping.types import From, To

print(From)
print(To)

from unipressed import IdMappingClient
request = IdMappingClient.submit(
    source="UniProtKB_AC-ID", dest="Gene_Name", ids={"A1L190", "A0JP26", "A0PK11"}
)

print(request.get_status())
import time
while request.get_status() != "FINISHED":
    time.sleep(1)
print(list(request.each_result()))
