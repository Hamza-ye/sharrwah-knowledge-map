<?php

namespace Alsharie\Jawali\Responses;

class JawaliResponse
{
    /**
     * The raw response data.
     *
     * @var array
     */
    protected $data;

    /**
     * Whether the response was successful.
     *
     * @var bool
     */
    protected $success;

    /**
     * Create a new response instance.
     *
     * @param array $response
     */
    public function __construct(array $response)
    {
        $this->data = $response;
        $this->success = $this->isSuccess();
    }

    /**
     * Get a value from the response body.
     *
     * @param string|null $attribute
     * @return mixed
     */
    public function getResponseBody(?string $attribute = null)
    {
        if ($attribute && isset($this->data['responseBody'][$attribute])) {
            return $this->data['responseBody'][$attribute];
        }
        
        return $this->data['responseBody'] ?? $this->data;
    }

    /**
     * Get a value from the response.
     *
     * @param string|null $attribute
     * @return mixed
     */
    public function getResponse(?string $attribute = null)
    {
        if ($attribute && isset($this->data[$attribute])) {
            return $this->data[$attribute];
        }
        
        return $this->data;
    }

    /**
     * Determine if the response was successful.
     *
     * @return bool
     */
    public function isSuccess(): bool
    {
        return isset($this->data['responseStatus']) && 
               isset($this->data['responseStatus']['systemStatus']) && 
               $this->data['responseStatus']['systemStatus'] == '0';
    }

    /**
     * Get the error message if the response was not successful.
     *
     * @return string|null
     */
    public function getErrorMessage(): ?string
    {
        if (!$this->isSuccess() && isset($this->data['responseStatus']['systemStatusDesc'])) {
            return $this->data['responseStatus']['systemStatusDesc'];
        }
        
        return null;
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