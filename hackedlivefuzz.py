#!/usr/bin/env python3

import socket
import subprocess
import asyncio

def fuzzer(target_ip, target_port):
    payload = b"A" * 1000  # Örnek olarak 1000 baytlık "A" karakterleri ile doldurulmuş bir payload
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        print("Bağlantı başarılı.")
        
        s.send(payload)
        print(f"{len(payload)} bayt veri gönderildi.")
        
        response = s.recv(1024)
        print("Cevap alındı:", response)
        
        if b"belirli_bir_cevap" in response:  # Cevapta belirli bir şey varsa
            print("Ağa girme işlemi yapılıyor...")
            subprocess.run(["komut"], shell=True)  # Burada istediğiniz ağ işlemlerini yapabilirsiniz.
            
    except Exception as e:
        print("Hata:", e)
    finally:
        s.close()

async def task1():
    mini_hex1 = bytes.fromhex('01 02 03 04 05')
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    mini_hex2 = bytes.fromhex('10 20 30 40 50')
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def task3():
    mini_hex3 = bytes.fromhex('AA BB CC DD EE')
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 completed")

async def main():
    await asyncio.gather(task1(), task2(), task3())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

if __name__ == "__main__":
    target_ip = input("Hedef IP adresini girin: ")
    target_port = int(input("Hedef port numarasını girin: "))
    
    fuzzer(target_ip, target_port)
