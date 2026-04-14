class DynamicArray {
private:
    int *arr;
    int size;
    int capacity;
public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        if (i >= 0 && i < size) {
            return arr[i];
        }
        return -1; 
    }

    void set(int i, int n) {
        if (i >= 0 && i < size) {
            arr[i] = n;
        }
    }

    void pushback(int n) {
        if (size == capacity) {
            capacity *= 2;
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        if (size > 0) {
            size--;
            return arr[size];
        }
        return -1; 
    }

    void resize() {
        int *temp = new int[size];
        for (int i = 0; i < size; i++) {
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = new int[capacity];
        for (int i = 0; i < size; i++) {
            arr[i] = temp[i];
        }
        delete[] temp;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
