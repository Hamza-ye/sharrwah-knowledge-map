<?php

namespace Alsharie\Jawali\Facades;

use Illuminate\Support\Facades\Facade;

/**
 * @method static \Alsharie\Jawali\Responses\JawaliLoginResponse loginToSystem()
 * @method static \Alsharie\Jawali\Responses\JawaliWalletAuthResponse walletAuthentication(?array $headerOverrides = [])
 * @method static \Alsharie\Jawali\Responses\JawaliEcommerceInquiryResponse ecommerceInquiry(string $voucher, string $receiverMobile, string $purpose = '', ?array $headerOverrides = [])
 * @method static \Alsharie\Jawali\Responses\JawaliEcommerceCashoutResponse ecommerceCashout(string $voucher, string $receiverMobile, string $purpose = '', ?array $headerOverrides = [])
 * @method static bool refreshTokens()
 *
 * @see \Alsharie\Jawali\Services\JawaliService
 */
class Jawali extends Facade
{
    protected static function getFacadeAccessor()
    {
        return 'jawali.service';
    }
}
