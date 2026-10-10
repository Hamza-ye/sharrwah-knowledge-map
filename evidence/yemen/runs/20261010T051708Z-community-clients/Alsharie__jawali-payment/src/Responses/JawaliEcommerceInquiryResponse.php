<?php

namespace Alsharie\Jawali\Responses;

class JawaliEcommerceInquiryResponse extends JawaliResponse
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
     * Get the transaction amount.
     *
     * @return string|null
     */
    public function getAmount(): ?string
    {
        return $this->getResponseBody('txnamount');
    }

    /**
     * Get the transaction currency.
     *
     * @return string|null
     */
    public function getCurrency(): ?string
    {
        return $this->getResponseBody('txncurrency');
    }

    /**
     * Get the transaction state.
     *
     * @return string|null
     */
    public function getState(): ?string
    {
        return $this->getResponseBody('state');
    }

    /**
     * Get the transaction reference.
     *
     * @return string|null
     */
    public function getTransactionRef(): ?string
    {
        return $this->getResponseBody('issuerTrxRef');
    }
    /**
     * Get the transaction date.
     *
     * @return string|null
     */
    public function getTransactionDate(): ?string
    {
        return $this->getResponseBody('trxDate');
    }
}