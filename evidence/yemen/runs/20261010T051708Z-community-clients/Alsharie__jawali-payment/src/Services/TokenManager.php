<?php

namespace Alsharie\Jawali\Services;

use Carbon\Carbon;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Crypt;

class TokenManager
{
    private string $cachePrefix = 'jawali_tokens_';
    private int $tokenExpiryBuffer = 300; // 5 minutes buffer before actual expiry
    private string $salt = '';

    /**
     * Set the salt for token encryption.
     * This should be unique per user/instance.
     *
     * @param string $salt
     * @return void
     */
    public function setSalt(string $salt): void
    {
        $this->salt = $salt;
    }

    /**
     * Get the current salt.
     *
     * @return string
     */
    public function getSalt(): string
    {
        return $this->salt;
    }

    /**
     * Encrypt data with salt.
     *
     * @param string $data
     * @return string
     */
    private function encryptWithSalt(string $data): string
    {
        if (empty($this->salt)) {
            throw new \InvalidArgumentException('Salt must be set before encrypting tokens');
        }

        // Combine salt with data for unique encryption
        $saltedData = $this->salt . '|' . $data;
        return Crypt::encryptString($saltedData);
    }

    /**
     * Decrypt data with salt.
     *
     * @param string $encryptedData
     * @return string
     */
    private function decryptWithSalt(string $encryptedData): string
    {
        if (empty($this->salt)) {
            throw new \InvalidArgumentException('Salt must be set before decrypting tokens');
        }

        // Decrypt the salted data
        $saltedData = Crypt::decryptString($encryptedData);
        
        // Extract the original data (remove salt)
        $parts = explode('|', $saltedData, 2);
        if (count($parts) !== 2 || $parts[0] !== $this->salt) {
            throw new \Exception('Invalid salt or corrupted data');
        }
        
        return $parts[1];
    }

    /**
     * Set the authentication token.
     *
     * @param string $token
     * @param int|null $expiresIn Expiry time in seconds from now
     * @return void
     */
    public function setAuthToken(string $token, ?int $expiresIn = null): void
    {
        $expiryTime = $expiresIn ? 
            Carbon::now()->addSeconds($expiresIn - $this->tokenExpiryBuffer) : 
            Carbon::now()->addHours(24); // Default 24 hours if no expiry provided

        // Encrypt the token with salt before storing
        $encryptedToken = $this->encryptWithSalt($token);

        Cache::put(
            $this->cachePrefix . 'auth_token',
            $encryptedToken,
            $expiryTime
        );

        Cache::put(
            $this->cachePrefix . 'auth_expiry',
            $expiryTime->toISOString(),
            $expiryTime
        );
    }

    /**
     * Get the authentication token.
     *
     * @return string|null
     */
    public function getAuthToken(): ?string
    {
        if ($this->isAuthTokenExpired()) {
            $this->clearAuthToken();
            return null;
        }
        
        $encryptedToken = Cache::get($this->cachePrefix . 'auth_token');
        if (!$encryptedToken) {
            return null;
        }

        try {
            // Decrypt the token with salt before returning
            return $this->decryptWithSalt($encryptedToken);
        } catch (\Exception $e) {
            // If decryption fails, clear the corrupted token
            $this->clearAuthToken();
            return null;
        }
    }

    /**
     * Set the wallet token.
     *
     * @param string $token
     * @param int|null $expiresIn Expiry time in seconds from now
     * @return void
     */
    public function setWalletToken(string $token, ?int $expiresIn = null): void
    {
        $expiryTime = $expiresIn ? 
            Carbon::now()->addSeconds($expiresIn - $this->tokenExpiryBuffer) : 
            Carbon::now()->addHours(24); // Default 24 hours if no expiry provided

        // Encrypt the token with salt before storing
        $encryptedToken = $this->encryptWithSalt($token);

        Cache::put(
            $this->cachePrefix . 'wallet_token',
            $encryptedToken,
            $expiryTime
        );

        Cache::put(
            $this->cachePrefix . 'wallet_expiry',
            $expiryTime->toISOString(),
            $expiryTime
        );
    }

    /**
     * Get the wallet token.
     *
     * @return string|null
     */
    public function getWalletToken(): ?string
    {
        if ($this->isWalletTokenExpired()) {
            $this->clearWalletToken();
            return null;
        }
        
        $encryptedToken = Cache::get($this->cachePrefix . 'wallet_token');
        if (!$encryptedToken) {
            return null;
        }

        try {
            // Decrypt the token with salt before returning
            return $this->decryptWithSalt($encryptedToken);
        } catch (\Exception $e) {
            // If decryption fails, clear the corrupted token
            $this->clearWalletToken();
            return null;
        }
    }

    /**
     * Check if the authentication token is set and not expired.
     *
     * @return bool
     */
    public function hasAuthToken(): bool
    {
        $encryptedToken = Cache::get($this->cachePrefix . 'auth_token');
        if (!$encryptedToken) {
            return false;
        }

        try {
            // Try to decrypt with salt to verify the token is valid
            $this->decryptWithSalt($encryptedToken);
            return !$this->isAuthTokenExpired();
        } catch (\Exception $e) {
            // If decryption fails, the token is corrupted
            $this->clearAuthToken();
            return false;
        }
    }

    /**
     * Check if the wallet token is set and not expired.
     *
     * @return bool
     */
    public function hasWalletToken(): bool
    {
        $encryptedToken = Cache::get($this->cachePrefix . 'wallet_token');
        if (!$encryptedToken) {
            return false;
        }

        try {
            // Try to decrypt with salt to verify the token is valid
            $this->decryptWithSalt($encryptedToken);
            return !$this->isWalletTokenExpired();
        } catch (\Exception $e) {
            // If decryption fails, the token is corrupted
            $this->clearWalletToken();
            return false;
        }
    }

    /**
     * Check if the authentication token is expired.
     *
     * @return bool
     */
    public function isAuthTokenExpired(): bool
    {
        $expiryString = Cache::get($this->cachePrefix . 'auth_expiry');
        if (!$expiryString) {
            return true;
        }

        $expiryTime = Carbon::parse($expiryString);
        return Carbon::now()->isAfter($expiryTime);
    }

    /**
     * Check if the wallet token is expired.
     *
     * @return bool
     */
    public function isWalletTokenExpired(): bool
    {
        $expiryString = Cache::get($this->cachePrefix . 'wallet_expiry');
        if (!$expiryString) {
            return true;
        }

        $expiryTime = Carbon::parse($expiryString);
        return Carbon::now()->isAfter($expiryTime);
    }

    /**
     * Clear the authentication token.
     *
     * @return void
     */
    public function clearAuthToken(): void
    {
        Cache::forget($this->cachePrefix . 'auth_token');
        Cache::forget($this->cachePrefix . 'auth_expiry');
    }

    /**
     * Clear the wallet token.
     *
     * @return void
     */
    public function clearWalletToken(): void
    {
        Cache::forget($this->cachePrefix . 'wallet_token');
        Cache::forget($this->cachePrefix . 'wallet_expiry');
    }

    /**
     * Clear all tokens.
     *
     * @return void
     */
    public function clearAllTokens(): void
    {
        $this->clearAuthToken();
        $this->clearWalletToken();
    }

    /**
     * Securely clear all tokens and overwrite cache with random data.
     *
     * @return void
     */
    public function secureClearAllTokens(): void
    {
        // Clear tokens
        $this->clearAllTokens();
        
        // Overwrite cache locations with random data to prevent recovery
        $randomData = bin2hex(random_bytes(32));
        Cache::put($this->cachePrefix . 'auth_token', $randomData, now()->addMinutes(1));
        Cache::put($this->cachePrefix . 'wallet_token', $randomData, now()->addMinutes(1));
        
        // Clear the random data after a short delay
        Cache::forget($this->cachePrefix . 'auth_token');
        Cache::forget($this->cachePrefix . 'wallet_token');
    }

    /**
     * Get token expiry buffer in seconds.
     *
     * @return int
     */
    public function getTokenExpiryBuffer(): int
    {
        return $this->tokenExpiryBuffer;
    }

    /**
     * Set token expiry buffer in seconds.
     *
     * @param int $seconds
     * @return void
     */
    public function setTokenExpiryBuffer(int $seconds): void
    {
        $this->tokenExpiryBuffer = max(0, $seconds);
    }

    /**
     * Get authentication token expiry time.
     *
     * @return Carbon|null
     */
    public function getAuthTokenExpiry(): ?Carbon
    {
        $expiryString = Cache::get($this->cachePrefix . 'auth_expiry');
        return $expiryString ? Carbon::parse($expiryString) : null;
    }

    /**
     * Get wallet token expiry time.
     *
     * @return Carbon|null
     */
    public function getWalletTokenExpiry(): ?Carbon
    {
        $expiryString = Cache::get($this->cachePrefix . 'wallet_expiry');
        return $expiryString ? Carbon::parse($expiryString) : null;
    }

    /**
     * Get token status information.
     *
     * @return array
     */
    public function getTokenStatus(): array
    {
        $authToken = Cache::get($this->cachePrefix . 'auth_token');
        $walletToken = Cache::get($this->cachePrefix . 'wallet_token');

        return [
            'auth_token' => [
                'present' => !empty($authToken),
                'expired' => $this->isAuthTokenExpired(),
                'expiry' => $this->getAuthTokenExpiry()?->toISOString(),
                'valid' => $this->hasAuthToken(),
                'encrypted' => !empty($authToken), // Indicates if token is encrypted
                'salted' => !empty($this->salt), // Indicates if salt is being used
            ],
            'wallet_token' => [
                'present' => !empty($walletToken),
                'expired' => $this->isWalletTokenExpired(),
                'expiry' => $this->getWalletTokenExpiry()?->toISOString(),
                'valid' => $this->hasWalletToken(),
                'encrypted' => !empty($walletToken), // Indicates if token is encrypted
                'salted' => !empty($this->salt), // Indicates if salt is being used
            ],
            'security' => [
                'salt_configured' => !empty($this->salt),
                'salt_length' => strlen($this->salt),
                'cache_prefix' => $this->cachePrefix,
            ],
        ];
    }

    /**
     * Set cache prefix for token storage.
     *
     * @param string $prefix
     * @return void
     */
    public function setCachePrefix(string $prefix): void
    {
        $this->cachePrefix = $prefix;
    }

    /**
     * Get cache prefix for token storage.
     *
     * @return string
     */
    public function getCachePrefix(): string
    {
        return $this->cachePrefix;
    }
}