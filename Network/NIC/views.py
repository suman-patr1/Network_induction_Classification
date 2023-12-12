from django.shortcuts import render

# Create your views here.
def nic(request):
    if request.method=='POST':
        d=request.POST
        n1=d.get('PN')
        n2=d.get('RP')
        n3=d.get('RB')
        n4=d.get('SP')
        n5=d.get('SB')
        n6=d.get('PAD')
        n7=d.get('DSB')
        n8=d.get('DSP')
        n9=d.get('DPAD')
        n10=d.get('CP')
        n11=d.get('AFE')
        n12=d.get('PLU')
        n13=d.get('PM')
        n14=d.get('LBC')
        if "btnpredict" in request.POST:
            import pandas as pd
            data=pd.read_csv('C:\\Users\\patra\\Dataset\\Net.csv')
            data=data.drop(['Packets Rx Dropped','Packets Tx Dropped','Packets Rx Errors','Packets Tx Errors','Delta Packets Rx Dropped',' Delta Packets Tx Dropped','Delta Packets Rx Errors','Delta Packets Tx Errors','Total Load/Rate','Total Load/Latest','Unknown Load/Rate','Unknown Load/Latest','is_valid','Table ID','Max Size','Delta Received Packets','Delta Received Bytes'],'columns')
            from sklearn.preprocessing import MinMaxScaler
            sc=MinMaxScaler()

            sc.fit(data[['Delta Port alive Duration (S)','Sent Packets','Received Packets','Received Bytes','Sent Bytes','Port alive Duration (S)','Delta Sent Bytes','Delta Sent Packets','Packets Looked Up','Packets Matched','Connection Point','Active Flow Entries','Latest bytes counter']])
            data[['Delta Port alive Duration (S)','Sent Packets','Received Packets','Received Bytes','Sent Bytes','Port alive Duration (S)','Delta Sent Bytes','Delta Sent Packets','Packets Looked Up','Packets Matched','Connection Point','Active Flow Entries','Latest bytes counter']]=sc.transform(data[['Active Flow Entries','Connection Point','Delta Port alive Duration (S)','Sent Packets','Received Packets','Received Bytes','Sent Bytes','Delta Sent Bytes','Delta Sent Packets','Delta Port alive Duration (S)','Packets Looked Up','Packets Matched','Latest bytes counter']])
            inputs=data.drop('Label','columns')
            output=data['Label']
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test= train_test_split(inputs,output,train_size=0.8)
            from sklearn.neighbors import KNeighborsClassifier
            model=KNeighborsClassifier(n_neighbors=71)
            model.fit(x_train,y_train)
            result=model.predict([[float(n1),float(n2),float(n3),float(n4),float(n5),float(n6),float(n7),float(n8),float(n9),float(n10),float(n11),float(n12),float(n13),float(n14)]])
    
    
            return render(request,'nic.html',context={'result':result})
    return render(request,'nic.html')