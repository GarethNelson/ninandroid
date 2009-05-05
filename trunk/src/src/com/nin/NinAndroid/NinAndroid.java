package com.nin.NinAndroid;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.widget.ImageView;
import android.widget.Toast;


public class NinAndroid extends Activity {
	private OnClickListener LoginClickListener = new OnClickListener() {
	    public void onClick(View v) {
	    	Toast.makeText(getApplicationContext(), "Login not yet implemented", Toast.LENGTH_SHORT).show();
	    }
	};
		
	WebView webview;
	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        webview = (WebView) findViewById(R.id.webview);
        webview.getSettings().setJavaScriptEnabled(true);
        webview.loadUrl("file:///android_asset/home.html");

        ImageView LoginButton = (ImageView)findViewById(R.id.LoginBtn);
        LoginButton.setOnClickListener(LoginClickListener);

    }
}