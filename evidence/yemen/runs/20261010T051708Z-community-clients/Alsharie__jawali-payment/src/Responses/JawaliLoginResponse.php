<?php

namespace Alsharie\Jawali\Responses;

class JawaliLoginResponse
{
    /**
     * The raw response data.
     *
     * @var array
     */
    protected $data;

    /**
     * Create a new response instance.
     *
     * @param array $response
     */
    public function __construct(array $response)
    {
        $this->data = $response;
    }

    /**
     * Get the access token.
     *
     * @return string|null
     */
    public function getAccessToken(): ?string
    {
        return $this->data['access_token'] ?? null;
    }

    /**
     * Get the refresh token.
     *
     * @return string|null
     */
    public function getRefreshToken(): ?string
    {
        return $this->data['refresh_token'] ?? null;
    }

    /**
     * Get the token type.
     *
     * @return string|null
     */
    public function getTokenType(): ?string
    {
        return $this->data['token_type'] ?? null;
    }

    /**
     * Get the expires in value.
     *
     * @return int|null
     */
    public function getExpiresIn(): ?int
    {
        return isset($this->data['expires_in']) ? (int) $this->data['expires_in'] : null;
    }

    /**
     * Determine if the response was successful.
     *
     * @return bool
     */
    public function isSuccess(): bool
    {
        return isset($this->data['access_token']);
    }

    /**
     * Get the raw data.
     *
     * @return array
     */
    public function getData(): array
    {
        return $this->data;
    }
}