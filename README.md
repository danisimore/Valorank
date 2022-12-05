## Last updated on December 5th
**:dart: Update target**:

+ add a 'store' page

**:heavy_check_mark: Changes**:
+ In **`store/models.py`**:
  + added ***"discount"***, ***"old_price"***, ***"execution_time"*** fields;
  + the ***"price"*** field has been renamed to ***"current price"***;
  
+ In **`store/admin.py`**:
  + New fields are registered in the admin panel; 
+ In **`store/views.py`**:
  + added `StoreFormView`;
+ Added **`urls.py`** to **`store`**;
+ Added **`forms.py`** to **`store`**;
+ In **`store/forms.py`**:
  + added `RankSelectionForm`;
+ In **`templates`**:
  + added templates for the store page;
+ In **`static/css`**:
  + added `store.css`;
+ *And also a few more minor changes.*
