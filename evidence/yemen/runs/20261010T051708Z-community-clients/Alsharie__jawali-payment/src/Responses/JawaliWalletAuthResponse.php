<?php

namespace Alsharie\Jawali\Responses;

class JawaliWalletAuthResponse extends JawaliResponse
{
    /**
     * Create a new response instance.
     *
     * @param array $response
     */
    public function __construct(array $response)
    {
        parent::__construct($response);
    }

    /**
     * Get the access token.
     *
     * @return string|null
     */
    public function getAccessToken(): ?string
    {
        return $this->getResponseBody('access_token');
    }

    /**
     * Get the organization value.
     *
     * @return string|null
     */
    public function getOrgValue(): ?string
    {
        return $this->getResponseBody('org_value');
    }

    /**
     * Get the organization name.
     *
     * @return string|null
     */
    public function getOrgName(): ?string
    {
        return $this->getResponseBody('org_name');
    }
}