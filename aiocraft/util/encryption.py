"""Minecraft encryption utilities. These are mostly pasted and edited from https://github.com/ammaraskar/pyCraft"""
# TODO read more about this, improve implementation if possible
import os
from hashlib import sha1

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_shared_secret() -> bytes:
	return os.urandom(16)


def create_AES_cipher(shared_secret:bytes) -> Cipher:
	return Cipher(algorithms.AES(shared_secret), modes.CFB8(shared_secret),
					backend=default_backend())

def encrypt_token_and_secret(pubkey, verification_token, shared_secret:bytes):
	pubkey = load_der_public_key(pubkey, default_backend())

	encrypted_token = pubkey.encrypt(verification_token, PKCS1v15())
	encrypted_secret = pubkey.encrypt(shared_secret, PKCS1v15())
	return encrypted_token, encrypted_secret

def generate_verification_hash(server_id, shared_secret, public_key) -> str:
	verification_hash = sha1()

	verification_hash.update(server_id.encode('utf-8'))
	verification_hash.update(shared_secret)
	verification_hash.update(public_key)

	return minecraft_sha1_hash_digest(verification_hash)

def minecraft_sha1_hash_digest(sha1_hash) -> str:
	return format(int.from_bytes(sha1_hash.digest(), byteorder='big', signed=True), 'x')
