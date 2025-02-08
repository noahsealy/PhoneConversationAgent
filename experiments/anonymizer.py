import re
import hashlib
from typing import Dict, Any

class Anonymizer:
    def __init__(self):
        self.mapping: Dict[str, str] = {}
        self._salt = "custom_salt_value"  # Change this in production

    def _hash_value(self, value: str) -> str:
        """Generate a consistent hash for a given value."""
        salted = f"{value}{self._salt}".encode('utf-8')
        return hashlib.md5(salted).hexdigest()[:8]

    def anonymize_email(self, email: str) -> str:
        """Anonymize an email address while preserving the domain."""
        if not email or '@' not in email:
            return email
        
        if email in self.mapping:
            return self.mapping[email]
        
        username, domain = email.split('@')
        anon_username = self._hash_value(username)
        anonymized = f"{anon_username}@{domain}"
        self.mapping[email] = anonymized
        return anonymized

    def anonymize_phone(self, phone: str) -> str:
        """Anonymize a phone number while preserving the format."""
        if not phone:
            return phone
        
        if phone in self.mapping:
            return self.mapping[phone]
        
        # Remove non-digit characters
        digits = re.sub(r'\D', '', phone)
        if not digits:
            return phone
        
        # Create a hash and use last N digits where N is the length of original digits
        hashed = self._hash_value(digits)
        anon_digits = hashed[-len(digits):]
        
        # Reconstruct the phone number format
        result = ''
        digit_idx = 0
        for char in phone:
            if char.isdigit():
                result += anon_digits[digit_idx]
                digit_idx += 1
            else:
                result += char
        
        self.mapping[phone] = result
        return result

    def anonymize_text(self, text: str) -> str:
        """Anonymize a piece of text by replacing known values with their anonymous versions."""
        if not text:
            return text
        
        if text in self.mapping:
            return self.mapping[text]
        
        # Create a hash of the entire text
        anonymized = self._hash_value(text)
        self.mapping[text] = anonymized
        return anonymized

    def clear_mapping(self):
        """Clear the stored mapping of original to anonymized values."""
        self.mapping.clear()
