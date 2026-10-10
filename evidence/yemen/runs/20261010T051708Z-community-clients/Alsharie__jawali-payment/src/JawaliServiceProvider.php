<?php

namespace Alsharie\Jawali;

use Alsharie\Jawali\Services\JawaliService;
use Illuminate\Support\ServiceProvider;

class JawaliServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->mergeConfigFrom(
            __DIR__.'/../config/jawali.php', 'jawali'
        );

        $this->app->singleton('jawali.service', function ($app) {
            return new JawaliService($app['config']['jawali']);
        });
    }

    public function boot()
    {
        if ($this->app->runningInConsole()) {
            $this->publishes([
                __DIR__.'/../config/jawali.php' => config_path('jawali.php'),
            ], 'jawali-config');
        }
    }
}