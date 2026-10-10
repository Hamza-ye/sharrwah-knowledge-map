<?php

namespace Alsharie\Jawali\Responses;

class JawaliEcommerceCashoutResponse extends JawaliResponse
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
     * Get the state .
     *
     * @return string|null
     */
    public function getStatue(): ?string
    {
        return $this->getResponseBody('status');
    }


    /**
     * Get the transaction amount.
     *
     * @return string|null
     */
    public function getAmount(): ?string
    {
        return $this->getResponseBody('amount');
    }

    /**
     * Get the wallet balance.
     *
     * @return string|null
     */
    public function getBalance(): ?string
    {
        return $this->getResponseBody('balance');
    }

    /**
     * Get the transaction reference.
     *
     * @return string|null
     */
    public function getTransactionRef(): ?string
    {
        return $this->getResponseBody('refId');
    }
    /**
     * Get the transaction reference.
     *
     * @return string|null
     */
    public function getIssuerRef(): ?string
    {
        return $this->getResponseBody('IssuerRef');
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