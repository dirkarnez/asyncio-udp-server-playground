# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import asyncio

class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print(f'Received {message} from {addr}')
        
        # Send response back
        print(f'Send {message} back to {addr}')
        self.transport.sendto(data, addr)

async def main():
    loop = asyncio.get_running_loop()
    
    # Start the server
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))
    
    print("Server started")
    
    # Run forever
    try:
        await asyncio.sleep(3600)
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())
