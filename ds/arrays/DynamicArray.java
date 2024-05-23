package arrays;

import java.util.Arrays;
import java.util.Comparator;
import java.util.function.Consumer;

public class DynamicArray<T> {
    private Object[] array;
    private int size;
    private static final int DEFAULT_CAPACITY = 10; 

    public DynamicArray() {
        this.array = new Object[DEFAULT_CAPACITY];
        this.size = 0;
    }

    public DynamicArray(int initialCapacity) {
        if (initialCapacity <= 0) {
            throw new IllegalArgumentException("Initial Capacity must be positive.");
        }

        this.array = new Object[initialCapacity];
        this.size = 0;
    }

    public void traverse() {
        for (int i = 0; i < size; i++) {
            System.out.println(array[i]);
        }
    }

    @SuppressWarnings("unchecked") // Because of unchecked type casting 
    public void traverse(Consumer<T> action) {
        for (int i = 0; i < size; i++) {
            action.accept((T) array[i]); // Casting to T before passing to the consumer function
        }
    }

    private void ensureCapacity() {
        if (size == array.length) {
            int newCapacity = array.length + DEFAULT_CAPACITY;
            array = Arrays.copyOf(array, newCapacity);
        }
    }

    private void ensureCapacity(int minCapacity) {
        if (minCapacity > array.length) {
            int newCapacity = Math.max(minCapacity, array.length + DEFAULT_CAPACITY);
            array = Arrays.copyOf(array, newCapacity);
        }
    }

    public void insert(T element) {
        ensureCapacity();
        array[size++] = element;
    }

    public void insert(T element, int index) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds.");
        }
        ensureCapacity();
        for (int i = size; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = element;
        size++;
    }

    public void extend(T[] newArray) {
        ensureCapacity(size + newArray.length);
        System.arraycopy(newArray, 0, array, size, newArray.length);
        size += newArray.length;
    }

    public void extend(T[] newArray, int index) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds.");
        }

        ensureCapacity(size + newArray.length);
        // Shift the existing elements to make room for the new array. 
        System.arraycopy(array, index, array, index + newArray.length, size - index);
        // Copy elements from the new array to the specified index. 
        System.arraycopy(newArray, 0, array, index, newArray.length);
        size += newArray.length;
    }


    public void delete(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds.");
        }

        for (int i = index; i < size - 1; i++) {
            array[i] = array[i + 1];
        }
        array[size - 1] = null;
        size--;
    }

    public void delete(int startIndex, int endIndex) {
        if (startIndex < 0 || startIndex >= size) {
            throw new IndexOutOfBoundsException("Invalid startIndex provided.");
        }
        if (endIndex < startIndex || endIndex >= size) {
            throw new IndexOutOfBoundsException("Invalid endIndex provided.");
        }

        int elementsToDelete = endIndex - startIndex + 1;
        System.arraycopy(array, endIndex + 1, array, startIndex, size - endIndex - 1);
        size -= elementsToDelete;

        // Set null to the remaining elements at the end. 
        Arrays.fill(array, size, size + elementsToDelete, null);
    }

    public void resize(int newCapacity) {
        if (newCapacity <= 0) {
            throw new IllegalArgumentException("Capacity must be postiive.");
        }
        array = Arrays.copyOf(array, newCapacity);
    }

    public void truncate(int newSize) {
        if (newSize < 0 || newSize > size) {
            throw new IllegalArgumentException("Invalid new size.");
        }
        size = newSize;
        array = Arrays.copyOf(array, size);
    }

    public void fill(T value) {
        Arrays.fill(array, 0, size, value);
    }

    public void fill(T value, int startIndex, int endIndex) {
        if (startIndex < 0 || startIndex >= size) {
            throw new IndexOutOfBoundsException("Invalid startIndex provided.");
        }
        if (endIndex < startIndex || endIndex >= size) {
            throw new IndexOutOfBoundsException("Invalid endIndex provided.");
        }

        Arrays.fill(array, startIndex, endIndex + 1, value);
    }

    public boolean search(T element) {
        for (int i = 0; i < size; i++) {
            if (array[i].equals(element)) {
                return true;
            }
        }
        return false;
    }

    private void swap(int i, int j) {
        Object temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    @SuppressWarnings("unchecked")
    public void sort(Comparator<T> comparator) {
        for (int i = 0; i < size - 1; i++) {
            for (int j = i + 1; j < size; j++) {
                if (comparator.compare((T) array[i], (T) array[j]) > 0) {
                    swap(i, j);
                }
            }
        }
    }

    @SuppressWarnings("unchecked")
    private int partition(int low, int high) {
        T pivot = (T) array[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (((Comparable<T>) array[j]).compareTo(pivot) < 0) {
                i++;
                swap(i, j);
            }
        }
        swap(i + 1, high);
        return i + 1;
    }

    public void quickSort(int low, int high) {
        if (low < high) {
            int partitionIndex = partition(low, high);
            quickSort(low, partitionIndex - 1);
            quickSort(partitionIndex + 1, high);
        }
    }
} 