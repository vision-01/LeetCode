import uuid

def generate_short_uuid(length=8):
    return str(uuid.uuid4()).replace('-', '')[:length]

if __name__ == "__main__":
    short_uuid = generate_short_uuid()
    print(f"Generated UUID of {len(short_uuid)} characters: {short_uuid}")