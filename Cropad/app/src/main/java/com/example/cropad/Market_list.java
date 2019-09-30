package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.ArrayList;

public class Market_list extends AppCompatActivity {

    RecyclerView recyclerView;
    ArrayList<marketdata> marketdataList;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_market_list);
        recyclerView = findViewById(R.id.market_list_recyclerview);
        btn=findViewById(R.id.marketButton);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                marketdataList=new ArrayList<>();
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));
                marketdataList.add(new marketdata("Vashi","5000"));

                LinearLayoutManager layoutManager=new LinearLayoutManager(getApplicationContext());
                RecyclerView.LayoutManager layoutManager1=layoutManager;
                MarketAdapter adapter= new MarketAdapter(getApplicationContext(), marketdataList);

                recyclerView.setLayoutManager(layoutManager1);
                recyclerView.setAdapter(adapter);

            }
        });


    }
}
